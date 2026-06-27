import datetime
import os

today = datetime.date.today().isoformat()

title = f"今日の自動記事 {today}"

content = f"""# {title}

これはAIで自動生成された記事です。

- 日付: {today}
- テーマ: 節約・投資・生活改善など

今日も小さく改善することが大事。
"""

filename = f"posts/{today}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)
