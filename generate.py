import os
import datetime

today = datetime.date.today().isoformat()

# ★これ追加（重要）
os.makedirs("posts", exist_ok=True)

filename = f"posts/{today}.md"

content = f"""# 今日の記事 {today}

これは自動生成された記事です。
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)
