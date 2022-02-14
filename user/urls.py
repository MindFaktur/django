from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='user_registration'),
    path('login/', views.UserLogin.as_view(), name='user_login'),
]