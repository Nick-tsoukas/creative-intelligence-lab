"""Optional real Chromium capture smoke. Synthetic HTML, no app/server/package install."""
from pathlib import Path
import importlib.util
import json
import os
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('capture_check', ROOT / 'skills/elite-ux-director/scripts/check_capture.py')
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)
chrome = Path(os.environ.get('CHROME_PATH', r'C:\Program Files\Google\Chrome\Application\chrome.exe'))
if not chrome.is_file():
    raise SystemExit('SKIP: Chrome unavailable; set CHROME_PATH to an existing Chromium executable')
out = ROOT / '.cil-private/v06-capture-smoke'
out.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(prefix='elite-ux-browser-') as temp:
    profile = Path(temp) / 'profile'
    for width in (390, 1440):
        for kind in ('good', 'black-tail'):
            page = Path(temp) / (kind + '.html')
            content = ''.join(f'<section><h2>Chapter {i}</h2><p>Original synthetic content for screenshot verification.</p><div class="image"></div></section>' for i in range(5 if kind == 'good' else 1))
            content = f'<style>main{{width:{width}px;box-sizing:border-box;margin:0}}</style>' + content
            page.write_text('<!doctype html><meta charset="utf-8"><title>Capture fixture</title><style>body{margin:0;min-height:1600px;background:#000;color:#f4f4f4;font:18px system-ui}main{padding:24px;max-width:900px;margin:auto}section{min-height:250px;border-bottom:1px solid #777}h1{font-size:36px}h2{font-size:24px}.image{height:70px;background:linear-gradient(90deg,#1b5b79,#af6850)}</style><main><h1>Screen evidence fixture</h1>' + content + '</main>', encoding='utf-8')
            image = out / f'{kind}-{width}.png'
            command = [str(chrome), '--headless=new', '--disable-background-networking', '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--disable-gpu', '--force-device-scale-factor=1', '--hide-scrollbars', '--virtual-time-budget=1500', '--run-all-compositor-stages-before-draw', f'--user-data-dir={profile}', f'--window-size={width},1600', f'--screenshot={image}', page.as_uri()]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=40)
            if result.returncode:
                raise RuntimeError('Chrome screenshot failed: ' + result.stderr.decode(errors='replace')[-500:])
            data = tool.inspect(image, width, 1600)
            expected = 'REVIEW_REQUIRED' if kind == 'black-tail' else 'NO_AUTOMATED_CONCERN'
            assert data['status'] == expected, data
            print(json.dumps(data))
print('PASS: actual Chromium PNGs at 390/1440; valid content and broken black-tail captures distinguished. Not product QA.')
