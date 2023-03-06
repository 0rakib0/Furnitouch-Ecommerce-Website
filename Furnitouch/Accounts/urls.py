from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.Regitration, name='register'),
    path('login/', views.User_login, name='login'),
]
