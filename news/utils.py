import requests
from decouple import config

API_KEY = config("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/"

def fetch_news(category=None, query=None, country="in", sources=None):
    # Default endpoint: top-headlines
    url = BASE_URL + "top-headlines?"
    params = {"apiKey": API_KEY}

    if sources:
        params["sources"] = sources
    else:
        params["country"] = country

    if category:
        params["category"] = category

    if query:
        # ✅ Switch to "everything" with stricter query
        url = BASE_URL + "everything?"
        params = {
            "qInTitle": query,   # stricter search
            "apiKey": API_KEY,
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": 15   # fetch up to 15 results
        }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print("Error:", response.status_code, response.json())
        return []
