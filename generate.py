import os
import datetime
import subprocess

today = datetime.date.today().isoformat()
os.makedirs("posts", exist_ok=True)

prompt = """
日本語でSEOブログ記事を書いてください。
テーマ：節約・投資・生活改善のどれか
見出し付きで800文字程度
"""

result = subprocess.run(
    ["ollama", "run", "mistral", prompt],
    capture_output=True,
    text=True
)

content = result.stdout

filename = f"posts/{today}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)
