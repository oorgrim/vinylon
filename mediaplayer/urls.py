from django.contrib import admin
from django.urls import path
from . import views

app_name = "mediaplayer"

urlpatterns = [
    path('',  views.MediaPlayerView.as_view(), name="mediaplayer"),
]