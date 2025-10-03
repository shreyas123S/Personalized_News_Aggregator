import requests

API_KEY = "96d84cbc9b6e4005b15cc0bbf736828d"
BASE_URL = "https://newsapi.org/v2/"

def fetch_news(category=None, query=None, country="us"):
    url = BASE_URL + "top-headlines?"
    params = {
        "apiKey": API_KEY,
        "country": country,
    }

    if category:
        params["category"] = category
    if query:
        url = BASE_URL + "everything?"
        params = {"q": query, "apiKey": API_KEY, "sortBy": "publishedAt"}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        return []
