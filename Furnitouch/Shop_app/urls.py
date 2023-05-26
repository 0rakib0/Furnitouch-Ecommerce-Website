from django.urls import path
from . import views

app_name = 'Shop_app'

urlpatterns = [
        path('shop-page/', views.Shop_page, name='shop_page')
]
