from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sports/", views.sports, name="sports"),
    path("cricket/", views.cricket, name="cricket"),
    path("technology/", views.technology, name="technology"),
    path("politics/", views.politics, name="politics"),
    path("entertainment/", views.entertainment, name="entertainment"),
    path("search/", views.search, name="search"),
]
