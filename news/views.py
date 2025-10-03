from django.shortcuts import render
from .utils import fetch_news

def search(request):
    query = request.GET.get("q")
    articles = []
    if query:
        raw_articles = fetch_news(query=query, country="in")
        # ✅ Extra filter: only keep articles that contain query in title/description
        articles = [
            a for a in raw_articles
            if query.lower() in (a.get("title", "").lower() + a.get("description", "").lower())
        ]
    return render(request, "news/home.html", {"articles": articles, "search_query": query})

def home(request):
    articles = fetch_news(country="us")
    return render(request, "news/home.html", {"articles": articles})

def sports(request):
    articles = fetch_news(category="sports", country="us")
    return render(request, "news/home.html", {"articles": articles})

def cricket(request):
    # Use category + keyword + India country to filter better
    articles = fetch_news(category="sports", query="cricket", country="in")
    return render(request, "news/home.html", {"articles": articles})

def technology(request):
    articles = fetch_news(category="technology", country="us")
    return render(request, "news/home.html", {"articles": articles})

def politics(request):
    articles = fetch_news(category="general", country="us")  # newsapi has no "politics", using general
    return render(request, "news/home.html", {"articles": articles})

def entertainment(request):
    articles = fetch_news(category="entertainment", country="us")
    return render(request, "news/home.html", {"articles": articles})
