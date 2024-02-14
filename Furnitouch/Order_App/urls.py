from django.urls import path
from . import views


app_name='order_app'

urlpatterns = [
    # ---------------------> Shopping Card <--------------------
        path('add_shopping-card-product/<slug:slug>/', views.Add_to_Card, name='add_product_card'),
        path('remove-card-item/<int:id>/', views.Remove_Product_from_Card, name='remove_card_item'),
        path('increase-quintity/<slug:slug>/', views.Increse_cart, name='increase_quintity'),
        path('dincrease-quintity/<slug:slug>/', views.Dicrease_card, name='dincrease_quintity'),
]
