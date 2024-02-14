from django.urls import path
from . import views


app_name = 'Home'


urlpatterns = [
    path('', views.Home, name='home'),
    path('new-arrival-product/', views.New_Product, name='new_product'),
    # path('category/', views.Category, name='category')
    
]
