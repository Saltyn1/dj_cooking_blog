from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegisterView, SignInView, profile

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),

]