import os
import datetime
import subprocess

today = datetime.date.today().isoformat()
os.makedirs("posts", exist_ok=True)

prompt = """
あなたはプロの日本語ブログライターです。

テーマは以下からランダムに1つ選んでください：
- 節約
- 投資
- 生活改善
- 副業

条件：
- SEOを意識
- タイトル付き
- 見出し付き（h2）
- 800〜1200文字
"""

result = subprocess.run(
    ["ollama", "run", "mistral", prompt],
    capture_output=True,
    text=True
)

# エラー対策（重要）
if result.returncode != 0:
    raise Exception("Ollama failed")

content = result.stdout.strip()

filename = f"posts/{today}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)
