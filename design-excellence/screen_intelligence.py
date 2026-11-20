#!/usr/bin/env python3
"""Read-only Nuxt/Vue screen inventory: static hints, not runtime data truth.

No network, server, paid API, dependency installs or model calls. Never executes code.
All information extracted by regex is marked STATIC_HINT_NOT_VERIFIED.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 256_000
MAX_FILES = 12
MAX_SCHEMAS = 6
EXTENSIONS = {".vue", ".ts", ".js", ".mjs"}
SUSPICIOUS = re.compile(r"(?:^|[/_.-])(secret|password|credential|token|private|\.env)(?:$|[/_.-])", re.I)
API_CALL = re.compile(r"(?<![\w$])(useFetch|useLazyFetch|\$fetch|useAsyncData|useLazyAsyncData|useStrapi|useStrapiClient)\s*(?:<[^()\n]{1,120}>)?\s*\(", re.M)
STATIC_URL = re.compile(r"""(?P<quote>['"\x60])(?P<url>/(?:api/)?[a-zA-Z0-9/_-]{1,150})(?P=quote)""")
COMPOSABLE = re.compile(r"\b(useState|useRoute|useRouter|useRuntimeConfig|useCookie|useNuxtApp|useFetch|useAsyncData|useLazyFetch|useLazyAsyncData|computed|ref|watch|onMounted|defineProps|defineEmits|useHead|navigateTo)\s*(?:<[^()\n]{1,120}>)?\s*\(")
IMPORT = re.compile(r"""(?:from\s*|import\s*\()\s*['"](?P<path>[^'"]{1,160})['"]""")
EVENT = re.compile(r'(?<![\w-])(?:@|v-on:)([a-z][a-z0-9-]{0,32})\s*=')
PROP = re.compile(r'(?<![\w-])(?:v-model(?::[\w-]+)?|:[a-z][\w-]*)\s*=')
FETCH_CONFIDENCE = "STATIC_HINT_NOT_VERIFIED"
SUPPORTED_EVIDENCE = {"CODE_OBSERVED", "RUNTIME_TESTED", "OWNER_CONFIRMED"}
FACT_KEYS = {"id", "kind", "name", "source", "used_for", "shape", "permissions", "states", "evidence", "verified_on"}
MANIFEST_KEYS = {"schema", "route", "facts", "unknowns", "constraints"}


def normalize_relative(root: Path, candidate: str) -> Path:
    if "\x00" in candidate or len(candidate) > 512:
        raise ValueError("Invalid path")
    rel = Path(candidate)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("Paths must be relative to repo root with no '..'")
    full = root.joinpath(rel)
    if not full.is_file() or full.is_symlink() or not full.resolve().is_relative_to(root):
        raise ValueError(f"Missing, symlinked or out-of-tree file: {candidate}")
    if full.suffix not in EXTENSIONS:
        raise ValueError(f"Unsupported source extension: {full.suffix}")
    if any(SUSPICIOUS.search(p) for p in rel.parts):
        raise ValueError("Refusing potentially secret-bearing source path")
    if full.stat().st_size > MAX_BYTES:
        raise ValueError("Source file exceeds 256KB safety cap")
    return full


def line_number(source: str, index: int) -> int:
    return source.count("\n", 0, index) + 1


def safe_path(value: str) -> str | None:
    """Only static API-like routes: deliberately skip query strings and dynamic URLs."""
    if not value.startswith("/") or value.endswith("/") or "//" in value or any(c in value for c in ("?", "#", "$", "{", "}", "%")):
        return None
    # Static route paths are not secrets, but only show routes, not response bodies.
    return value


def scan_file(root: Path, path: Path) -> dict:
    source = path.read_text(encoding="utf-8")
    rel = path.relative_to(root).as_posix()
    api: list[dict] = []
    for match in API_CALL.finditer(source):
        nearby = source[match.end():match.end() + 260]
        url = STATIC_URL.search(nearby)
        endpoint = safe_path(url.group("url")) if url and url.start() < 130 else None
        if url and nearby[url.end():].lstrip().startswith("+"):
            endpoint = None  # A literal concatenated with runtime values is not a static endpoint.
        api.append({
            "function": match.group(1), "static_path": endpoint,
            "line": line_number(source, match.start()),
            "note": "This identifies a callsite, not a successful request, schema or server permission",
            "evidence": FETCH_CONFIDENCE,
        })
    composables = sorted({m.group(1) for m in COMPOSABLE.finditer(source)})
    relative_imports = []
    for m in IMPORT.finditer(source):
        value = m.group("path")
        if value.startswith(("./", "../", "~/", "@/")) and not any(SUSPICIOUS.search(p) for p in Path(value).parts):
            relative_imports.append(value[:160])
    return {
        "file": rel,
        "evidence": FETCH_CONFIDENCE,
        "api_calls": api[:32],
        "composables": composables,
        "relative_imports": list(dict.fromkeys(relative_imports))[:30],
        "ui_events": sorted(set(EVENT.findall(source)))[:30],
        "bound_attributes": len(PROP.findall(source)),
        "notes": ["Static regex inspection; no execution, browser test or server authorization check"],
    }



def inspect_strapi_schema(root: Path, rel: str) -> dict:
    """Inspect ONLY explicit Strapi schema JSON: no database/user data or permission claims."""
    if "\x00" in rel or len(rel) > 512:
        raise ValueError("Invalid schema path")
    path = Path(rel)
    if path.is_absolute() or ".." in path.parts or path.suffix != ".json":
        raise ValueError("Strapi schema must be a relative .json path without traversal")
    if any(SUSPICIOUS.search(part) for part in path.parts):
        raise ValueError("Refusing secret-bearing schema path")
    root = root.resolve(strict=True)
    full = root / path
    if (not full.is_file() or full.is_symlink() or
            not full.resolve().is_relative_to(root) or full.stat().st_size > 128_000):
        raise ValueError("Missing, unsafe or oversized Strapi schema")
    doc = json.loads(full.read_text(encoding="utf-8"))
    if not isinstance(doc, dict) or not isinstance(doc.get("attributes"), dict):
        raise ValueError("Schema has no Strapi attributes object")
    attrs = doc["attributes"]
    if len(attrs) > 200:
        raise ValueError("Schema exceeds bounded field count")
    fields = []
    for key in sorted(attrs):
        entry = attrs[key]
        if not isinstance(key, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,79}", key) or not isinstance(entry, dict):
            raise ValueError("Malformed Strapi attribute")
        detail = {}
        for item in ("type", "relation", "target", "component"):
            value = entry.get(item)
            if isinstance(value, str):
                detail[item] = value[:160]
        for item in ("required", "private", "repeatable", "multiple"):
            value = entry.get(item)
            if isinstance(value, bool):
                detail[item] = value
        fields.append({"name": key, **detail})
    display = doc.get("info", {}).get("displayName", "") if isinstance(doc.get("info"), dict) else ""
    return {
        "file": rel,
        "display_name": str(display)[:120],
        "fields": fields,
        "evidence": "SCHEMA_OBSERVED_NOT_RESPONSE_OR_PERMISSION",
        "caution": "An attribute definition does not establish populated fields, serialization, user access, or server-side authorization",
    }


def validate_manifest(doc: dict, route: str) -> dict:
    if not isinstance(doc, dict) or set(doc) != MANIFEST_KEYS or doc.get("schema") != 1:
        raise ValueError("Manifest requires schema=1, route, facts, unknowns, constraints")
    if doc["route"] != route:
        raise ValueError("Manifest route does not match requested screen path")
    if not isinstance(doc["facts"], list) or len(doc["facts"]) > 60:
        raise ValueError("Invalid manifest facts")
    for fact in doc["facts"]:
        if not isinstance(fact, dict) or set(fact) != FACT_KEYS:
            raise ValueError("Fact needs id/kind/name/source/used_for/shape/permissions/states/evidence/verified_on")
        if not isinstance(fact["evidence"], str) or fact["evidence"] not in SUPPORTED_EVIDENCE:
            raise ValueError("Invalid fact evidence")
        for key, value in fact.items():
            if not isinstance(value, str) or len(value) > 600 or "\x00" in value:
                raise ValueError(f"Invalid fact field: {key}")
        if not fact["id"] or not fact["name"] or not fact["source"]:
            raise ValueError("Fact requires id, name and source")
    for key in ("unknowns", "constraints"):
        if not isinstance(doc[key], list) or len(doc[key]) > 50:
            raise ValueError(f"Invalid {key}")
        if any(not isinstance(item, str) or not item.strip() or len(item) > 600 for item in doc[key]):
            raise ValueError(f"Invalid {key} item")
    return doc


def inventory(root: Path, screen: str, includes: list[str], manifest_path: str | None = None,
              backend_root: Path | None = None, schema_paths: list[str] | None = None) -> dict:
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Repository root must be a directory")
    requested = [screen, *includes]
    if len(requested) > MAX_FILES:
        raise ValueError(f"At most {MAX_FILES} source files are allowed")
    unique = list(dict.fromkeys(requested))
    files = [normalize_relative(root, p) for p in unique]
    facts = []
    unknowns = [
        "Actual response payloads and backend authorization NOT VERIFIED",
        "Runtime state transitions, empty/error states and conditional access NOT TESTED",
        "Any computed dynamic endpoint cannot be resolved by this static scanner",
        "Data field names and permissions must be confirmed from real code or API tests",
    ]
    constraints = []
    if manifest_path:
        path = Path(manifest_path).expanduser()
        if not path.is_file() or path.is_symlink() or path.stat().st_size > 128_000:
            raise ValueError("Unsafe or missing manifest")
        manifest = validate_manifest(json.loads(path.read_text(encoding="utf-8")), screen)
        facts = manifest["facts"]
        unknowns = list(dict.fromkeys(unknowns + manifest["unknowns"]))
        constraints = manifest["constraints"]
    scanned = [scan_file(root, p) for p in files]
    selected_schemas = schema_paths or []
    if len(selected_schemas) > MAX_SCHEMAS:
        raise ValueError("Select at most six Strapi schema files")
    if selected_schemas and backend_root is None:
        raise ValueError("--backend-root required when --schema is provided")
    schemas = [inspect_strapi_schema(backend_root, path) for path in selected_schemas]
    if schemas:
        unknowns.append("Strapi content-type definitions are NOT evidence of API responses or user permissions")
    return {
        "schema": 1,
        "purpose": "SCREEN_IMPLEMENTATION_CONTEXT_NOT_A_SECURITY_AUDIT",
        "screen": screen,
        "files_scanned": len(scanned),
        "static_hints": scanned,
        "backend_schema_hints": schemas,
        "confirmed_or_observed_facts": facts,
        "constraints": constraints,
        "unknowns": unknowns,
        "implementation_rule": "Keep real props, APIs, data, roles, and state behavior; verify before implementing changes",
        "no_code_executed": True,
    }


def render_markdown(data: dict) -> str:
    lines = [
        "# Screen Intelligence — " + data["screen"], "",
        "**All scanned callsites and symbols are STATIC_HINT_NOT_VERIFIED.** No code or endpoint was executed.", "",
        "## Existing source and UI interaction clues",
    ]
    for file in data["static_hints"]:
        lines.append("\n### " + file["file"])
        lines.append("- Composables: " + (", ".join(file["composables"]) or "none detected"))
        lines.append("- UI events: " + (", ".join(file["ui_events"]) or "none detected"))
        lines.append("- Bound attributes detected: " + str(file["bound_attributes"]))
        for call in file["api_calls"]:
            lines.append(f"- API hint L{call['line']}: {call['function']} → {call['static_path'] or 'DYNAMIC/UNKNOWN'} (UNVERIFIED)")
        for imported in file["relative_imports"]:
            lines.append("- Import hint: " + imported)
    lines += ["", "## Selected Strapi content-type schema (field types only; no access inferred)"]
    if not data["backend_schema_hints"]:
        lines.append("- No backend content-type schema explicitly inspected.")
    for model in data["backend_schema_hints"]:
        lines.append("\n### " + model["file"] + " [" + model["evidence"] + "]")
        lines.append("- Model: " + (model["display_name"] or "UNNAMED"))
        for field in model["fields"]:
            details = ", ".join(k + "=" + str(v) for k, v in field.items() if k != "name")
            lines.append("- " + field["name"] + ": " + (details or "type UNKNOWN"))
        lines.append("- No verified API response/permission from schema alone.")
    lines += ["", "## Explicitly recorded data, states and authority"]
    if not data["confirmed_or_observed_facts"]:
        lines.append("- No verified field or permission contract provided yet.")
    for fact in data["confirmed_or_observed_facts"]:
        lines.extend([
            f"### {fact['kind']} — {fact['name']} [{fact['evidence']}]",
            f"- Source: {fact['source']}; verified on: {fact['verified_on'] or 'NOT STATED'}",
            f"- Purpose: {fact['used_for'] or 'NOT STATED'}; shape: {fact['shape'] or 'UNKNOWN'}",
            f"- Permissions: {fact['permissions'] or 'UNKNOWN'}",
            f"- States: {fact['states'] or 'NOT DOCUMENTED'}",
        ])
    lines += ["", "## Preserve these constraints", *(["- " + s for s in data["constraints"]] or ["- Not yet provided"]),
              "", "## Unknowns / mandatory verification", *["- " + s for s in data["unknowns"]], "",
              "**Before redesigning:** verify screen rendering, API shape, actual authorization, data presence, draft/publish flow and error/retry states in authorized dev. Do not infer that an icon is functional."]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", type=Path, required=True)
    p.add_argument("--screen", required=True, help="Relative path to actual Vue/Nuxt screen")
    p.add_argument("--include", action="append", default=[], help="Additional explicitly selected Vue/TS/JS file; max 11")
    p.add_argument("--manifest", help="Optional human-verified JSON screen contract")
    p.add_argument("--backend-root", type=Path, help="Optional checkout with Strapi source schemas")
    p.add_argument("--schema", action="append", default=[], help="Explicit relative Strapi content-type schema.json, max 6")
    p.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = p.parse_args(argv)
    try:
        result = inventory(args.repo_root, args.screen, args.include, args.manifest,
                           args.backend_root, args.schema)
        print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else render_markdown(result))
        return 0
    except (ValueError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
