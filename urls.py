from django.urls import path, include
from . import views

urlpatterns = [
    path('registration/', views.user_registration, name='user_registration'),
    path('login/', views.login, name='user_login'),
    path('details/', views.get_user_details, name='user_details'),
]