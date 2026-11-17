#!/usr/bin/env python3
"""Offline capture sanity check; stdlib only. Not a visual-quality certificate.

Exit 0: no automated concern; 1: invalid/dimension mismatch; 2: review flat tail.
Supports noninterlaced 8-bit RGB/RGBA PNGs from browser screenshot tools.
"""
import argparse
import json
import struct
import zlib
from pathlib import Path

MAX_PIXELS = 30_000_000
MAX_BYTES = 32 * 1024 * 1024


def paeth(a, b, c):
    p = a + b - c
    distances = (abs(p - a), abs(p - b), abs(p - c))
    return (a, b, c)[distances.index(min(distances))]


def inspect(path, expected_width=None, expected_height=None):
    path = Path(path)
    if path.stat().st_size > MAX_BYTES:
        raise ValueError('PNG exceeds 32 MiB; use overlapping capture segments')
    blob = path.read_bytes()
    if not blob.startswith(b'\x89PNG\r\n\x1a\n'):
        raise ValueError('Expected a PNG screenshot')
    pos, header, packed, ended = 8, None, bytearray(), False
    while pos < len(blob):
        if pos + 12 > len(blob):
            raise ValueError('Truncated PNG chunk')
        size = struct.unpack('>I', blob[pos:pos + 4])[0]
        tag = blob[pos + 4:pos + 8]
        end = pos + 12 + size
        if end > len(blob):
            raise ValueError('Truncated PNG payload')
        data = blob[pos + 8:pos + 8 + size]
        crc = struct.unpack('>I', blob[pos + 8 + size:end])[0]
        if zlib.crc32(tag + data) != crc:
            raise ValueError('PNG CRC mismatch')
        if tag == b'IHDR':
            if header is not None or pos != 8 or size != 13:
                raise ValueError('Invalid PNG header')
            header = struct.unpack('>IIBBBBB', data)
        elif tag == b'IDAT':
            if header is None:
                raise ValueError('PNG data before header')
            packed.extend(data)
        elif tag == b'IEND':
            if size or end != len(blob):
                raise ValueError('Invalid PNG end')
            ended = True
            break
        elif tag == b'acTL':
            raise ValueError('Animated PNG unsupported; capture a static PNG')
        elif tag[0] & 32 == 0:
            raise ValueError('Unsupported critical PNG chunk')
        pos = end
    if not header or not packed or not ended:
        raise ValueError('Incomplete PNG')
    w, h, depth, kind, comp, filt, interlace = header
    if not w or not h or w * h > MAX_PIXELS:
        raise ValueError('Image exceeds pixel bounds; use segmented captures')
    if depth != 8 or kind not in (2, 6) or comp or filt or interlace:
        raise ValueError('Use noninterlaced 8-bit RGB/RGBA PNG')
    if expected_width is not None and w != expected_width:
        raise ValueError(f'Width {w} differs from expected {expected_width}')
    if expected_height is not None and h != expected_height:
        raise ValueError(f'Height {h} differs from expected {expected_height}')
    channels = 3 if kind == 2 else 4
    stride = w * channels
    limit = (stride + 1) * h
    decoder = zlib.decompressobj()
    raw = decoder.decompress(packed, limit + 1)
    if len(raw) != limit or not decoder.eof or decoder.unused_data or decoder.unconsumed_tail:
        raise ValueError('Invalid or oversized PNG pixel stream')
    previous = bytearray(stride)
    tail, tail_color, translucent = 0, None, False
    for y in range(h):
        start = y * (stride + 1)
        filter_type = raw[start]
        if filter_type > 4:
            raise ValueError('Invalid PNG row filter')
        row = bytearray(raw[start + 1:start + 1 + stride])
        if filter_type:
            for i in range(stride):
                a = row[i - channels] if i >= channels else 0
                b = previous[i]
                c = previous[i - channels] if i >= channels else 0
                predictor = a if filter_type == 1 else b if filter_type == 2 else (a + b) // 2 if filter_type == 3 else paeth(a, b, c)
                row[i] = (row[i] + predictor) & 255
        # Bounded horizontal sampling after full decode, compositing alpha on white.
        colors = []
        for x in range(0, w, max(1, w // 96)):
            i = x * channels
            alpha = row[i + 3] if channels == 4 else 255
            translucent |= alpha < 255
            colors.append(tuple((v * alpha + 255 * (255 - alpha)) // 255 for v in row[i:i + 3]))
        flat = all(max(c[j] for c in colors) - min(c[j] for c in colors) <= 3 for j in range(3))
        center = colors[len(colors) // 2]
        if flat and (tail_color is None or max(abs(center[j] - tail_color[j]) for j in range(3)) <= 3):
            tail += 1
        elif flat:
            tail, tail_color = 1, center
        else:
            tail, tail_color = 0, None
        if flat and tail_color is None:
            tail_color = center
        previous = row
    suspicious = tail >= max(40, int(h * 0.30))
    warnings = []
    if suspicious:
        warnings.append('Large nearly uniform bottom region: inspect pixels or recapture the actual scroller')
    if translucent:
        warnings.append('Transparency found: verify intended background and visible content')
    return {'file': str(path), 'width': w, 'height': h,
            'flat_tail_rows': tail, 'status': 'REVIEW_REQUIRED' if warnings else 'NO_AUTOMATED_CONCERN',
            'warnings': warnings, 'visual_inspection_required': True}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('png', type=Path)
    parser.add_argument('--expected-width', type=int)
    parser.add_argument('--expected-height', type=int)
    args = parser.parse_args(argv)
    try:
        result = inspect(args.png, args.expected_width, args.expected_height)
    except (ValueError, OSError, zlib.error, struct.error) as error:
        print(json.dumps({'status': 'INVALID', 'error': str(error)}))
        return 1
    print(json.dumps(result))
    return 2 if result['status'] == 'REVIEW_REQUIRED' else 0


if __name__ == '__main__':
    raise SystemExit(main())
