from django.urls import path
from . import views

app_name = 'Shop_app'

urlpatterns = [
        path('shop-page/', views.Shop_page, name='shop_page'),
        path('single-product/<slug:slug>/', views.Single_Product, name='single_product'),
        # -------------------> Wish List <----------------------
        path('wishlist/', views.Wish_list, name='wishlist'),
        path('Add-wishlist/<slug:slug>/', views.Add_Widhlist, name='add_wishlist'),
        path('remove-wishlist/<int:id>/', views.Remove_Wish_List, name='remove_wishlist'),
        # ---------------------> Shopping Card <--------------------
        path('shoping-card/', views.Shopping_Card, name='shoping_card'),
        # path('add_shopping-card-product/<slug:slug>/', views.Add_product_card, name='add_product_card'),
        # path('remove-card-item/<int:id>/', views.Remove_Product_from_Card, name='remove_card_item'),
        # path('increase-quintity/<int:id>/', views.Increas_quintity, name='increase_quintity'),
]
