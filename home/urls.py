from django.urls import path
from .views import HomePageView
from . import views

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]