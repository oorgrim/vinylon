from django.urls import path
from . import views
from .views import dashboard, edit_profile
from .views import (
UserProfileView, RegisterView, UserLoginView,
UserLogoutView, UserPasswordChangeView, HomePageView 
)
# from django .conf import settings
# from django .conf.urls.static import static
app_name = 'users'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  

path('profile/', UserProfileView.as_view(), name='profile'),
path('register/', RegisterView.as_view(), name='register'),
path('login/', UserLoginView.as_view(), name='login'),
path('logout/', UserLogoutView.as_view(), name='logout'),
path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
path('dashboard/', dashboard, name='dashboard'),
path('edit-profile/', edit_profile, name='edit_profile'),
path('clear_avatar/', views.clear_avatar, name='clear_avatar'),  



]

# urlpatterns = [

# ] + static(settings.MEDIA_URL, document_root=settings.media)