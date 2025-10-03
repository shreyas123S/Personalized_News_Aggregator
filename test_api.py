import requests
from datetime import datetime, timezone

API_KEY = "96d84cbc9b6e4005b15cc0bbf736828d"

# Get today's date (UTC)
today = datetime.now(timezone.utc).date().isoformat()

# Search cricket news from Australian sources
url = (
    "https://newsapi.org/v2/everything?"
    "q=cricket&"
    "sortBy=publishedAt&"
    f"apiKey={API_KEY}"
)


response = requests.get(url)
print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    articles = data.get("articles", [])
    print(f"Cricket News in Australia Today: {len(articles)}\n")
    for art in articles[:5]:
        title = art.get("title")
        published = art.get("publishedAt")
        source = art.get("source", {}).get("name")
        print(f"- {title}\n  📰 {source} | 🕒 {published}\n")
else:
    print("Error:", response.json())
