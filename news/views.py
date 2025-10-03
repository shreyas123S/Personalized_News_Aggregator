from django.shortcuts import render
from .utils import fetch_news

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
