from django.contrib import admin
from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    path('', views.CatalogueView.as_view(), name="catalogue"),
    path('mediaplayer',  views.MediaPlayerView.as_view(), name="mediaplayer"),
    path('vinyl/<int:pk>/', views.VinylView, name="vinyl"),
]