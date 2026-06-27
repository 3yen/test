import os

POSTS_DIR = "posts"

files = sorted(
    [f for f in os.listdir(POSTS_DIR) if f.endswith(".md")],
    reverse=True
)

cards = ""

for f in files:
    title = f.replace(".md", "")
    cards += f"""
<div class="card">
  <h2>{title}</h2>
  <p>自動生成記事</p>
  <a class="btn" href="posts/{f}">読む</a>
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>マイル・ポイ活研究所</title>
<style>
body{{font-family:system-ui,sans-serif;max-width:900px;margin:auto;padding:20px;line-height:1.7}}
header{{background:#0b6efd;color:#fff;padding:24px;border-radius:12px}}
.card{{border:1px solid #ddd;border-radius:10px;padding:16px;margin:18px 0}}
.btn{{display:inline-block;background:#ff7a00;color:#fff;text-decoration:none;padding:10px 16px;border-radius:8px}}
footer{{margin-top:30px;color:#666;font-size:.9em}}
</style>
</head>
<body>

<header>
<h1>マイル・ポイ活研究所</h1>
<p>AIで自動生成されるブログ</p>
</header>

{cards}

<footer>
※自動生成サイトです
</footer>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated")
