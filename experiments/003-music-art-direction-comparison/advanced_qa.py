"""Experiment 003 advanced Chromium source-level DOM QA.

Run with: python advanced_qa.py --html /path/to/index.html
Requires playwright Python package and a local Chromium executable.
This performs basic semantic/viewport checks, NOT accessibility conformance.
"""
import argparse, json
from pathlib import Path
from playwright.sync_api import sync_playwright

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--html",type=Path,required=True,help="experiment HTML (from sandbox package)")
    parser.add_argument("--output",type=Path,default=Path("advanced_results.json"))
    parser.add_argument("--chromium",default=None,help="optional local executable; omit for Playwright-managed browser")
    args=parser.parse_args()
    html=args.html.read_text(encoding="utf-8")
    results=[]
    with sync_playwright() as p:
        launch_options={"args":["--no-sandbox"]}
        if args.chromium: launch_options["executable_path"]=args.chromium
        browser=p.chromium.launch(**launch_options)
        for width,height in [(320,640),(390,844),(768,900),(1280,800)]:
            for mode in ["baseline","direction"]:
                page=browser.new_page(viewport={"width":width,"height":height},device_scale_factor=1)
                errors=[]
                page.on("pageerror",lambda err:errors.append(str(err)))
                page.set_content(html)
                page.locator("#mode").select_option(mode)
                metrics=page.evaluate("""() => {
                  const els=[...document.querySelectorAll('a,button,select,input')].filter(e=>{
                    const r=e.getBoundingClientRect(),s=getComputedStyle(e);
                    return r.width>0&&r.height>0&&s.display!=='none'&&s.visibility!=='hidden';
                  });
                  const unlabeled=els.filter(e=>!e.getAttribute('aria-label')&&!e.innerText?.trim()&&!e.labels?.length&&!e.title);
                  const brokenHashes=[...document.querySelectorAll('a[href^="#"]')].filter(e=>e.getAttribute('href')!=='#'&&!document.getElementById(e.getAttribute('href').slice(1))).map(e=>e.outerHTML.slice(0,90));
                  return {scrollWidth:document.documentElement.scrollWidth,viewportWidth:document.documentElement.clientWidth,unlabeled:unlabeled.map(e=>e.outerHTML.slice(0,100)),brokenHashes,headings:[...document.querySelectorAll('h1')].map(e=>e.textContent.trim()),main:!!document.querySelector('main')};
                }""")
                page.locator("#mode").focus()
                focused=page.evaluate('document.activeElement===document.getElementById("mode")')
                page.emulate_media(reduced_motion="reduce")
                reduced=page.evaluate('matchMedia("(prefers-reduced-motion: reduce)").matches')
                passed=(metrics["scrollWidth"]<=metrics["viewportWidth"] and metrics["main"] and len(metrics["headings"])==1 and not metrics["unlabeled"] and not metrics["brokenHashes"] and not errors and focused and reduced)
                results.append({"width":width,"mode":mode,**metrics,"focus":focused,"reducedMotionMedia":reduced,"jsErrors":errors,"passedBasic":passed})
                page.close()
        browser.close()
    args.output.write_text(json.dumps(results,indent=2),encoding="utf-8")
    passed=sum(x["passedBasic"] for x in results)
    print(f"Basic DOM/viewport checks: {passed}/{len(results)}")
    if passed!=len(results): raise SystemExit(1)

if __name__=="__main__": main()
