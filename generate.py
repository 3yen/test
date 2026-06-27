from openai import OpenAI
import os
import datetime

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

today = datetime.date.today().isoformat()
os.makedirs("posts", exist_ok=True)

prompt = "日本語でSEOブログ記事を書いてください。テーマは節約・投資・生活改善のどれか。"

res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

content = res.choices[0].message.content

with open(f"posts/{today}.md", "w", encoding="utf-8") as f:
    f.write(content)
