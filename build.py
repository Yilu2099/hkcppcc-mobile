#!/usr/bin/env python3
"""把 src/index.template.html 裡的 {{IMG_*}} 佔位符替換成 assets/images.json 的 base64 圖片，輸出 index.html"""
import json, pathlib
root = pathlib.Path(__file__).parent
imgs = json.load(open(root/'assets/images.json'))
html = (root/'src/index.template.html').read_text(encoding='utf-8')
for k, v in imgs.items():
    html = html.replace('{{IMG_%s}}' % k.upper(), v)

# 簡繁字表：用 zhconv 把模板裡出現過的每個漢字轉成簡體，只保留有差異的字（約幾百對）
import re, json as _json
try:
    import zhconv
except ImportError:
    import subprocess, sys; subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'zhconv']); import zhconv
chars = sorted(set(re.findall(r'[\u3400-\u9fff]', html)))
t2s = {c: zhconv.convert(c, 'zh-cn') for c in chars}
t2s = {c: s for c, s in t2s.items() if s != c}
html = html.replace('{{T2S}}', _json.dumps(t2s, ensure_ascii=False, separators=(',', ':')))
print('簡繁字表', len(t2s), '對')
(root/'index.html').write_text(html, encoding='utf-8')
print('index.html', len(html)//1024, 'KB; leftover placeholders:', html.count('{{IMG_'))

# 另外輸出可直接雙擊/手機打開的完整檔案（Artifact 發佈時會自動加上 doctype/head，這裡手動補上）
wrapped = ('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           '<meta name="color-scheme" content="light dark"></head><body style="margin:0">' + html + '</body></html>')
(root/'preview.html').write_text(wrapped, encoding='utf-8')
(root/'docs').mkdir(exist_ok=True)
(root/'docs/index.html').write_text(wrapped, encoding='utf-8')  # GitHub Pages 發佈目錄
print('preview.html + docs/index.html written')
