from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('Account/', views.Account, name='accounts'),
    path('register/', views.Regitration, name='register'),
    path('login/', views.User_login, name='login'),
    path('logout/', views.User_logout, name='logout'),
    path('profile/', views.User_Profile, name='profile'),
    path('my-order/', views.myOrder, name='my_order')
]
