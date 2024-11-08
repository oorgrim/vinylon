from django.contrib import admin
from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    path('', views.CatalogueView.as_view(), name="catalogue"),
    path('<int:pk>/', views.VinylDetail.as_view(), name="vinyldetail"),
]