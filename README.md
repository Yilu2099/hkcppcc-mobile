# 港區省級政協委員聯誼會 · 手機版官網原型

- `src/index.template.html` — 唯一需要編輯的源檔（樣式、頁面結構、內容資料都在這裡）
- `assets/images.json` — 圖片的 base64（來自 hkcppcc.org 現站），`assets/photos/` 為原圖
- `build.py` — 把圖片注入模板，產出 `index.html`（供 Artifact 發佈）與 `preview.html`（可直接用瀏覽器 / 手機打開）

```bash
python3 build.py
```

公網網址（GitHub Pages，`docs/` 目錄）：https://yilu2099.github.io/hkcppcc-mobile/
Artifact 預覽：https://claude.ai/code/artifact/feb5083a-846c-4fff-b496-6ae8ca11be8a

更新上線：`python3 build.py && git add -A && git commit -m "update" && git push`
