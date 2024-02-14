from django.urls import path
from . import views

app_name = 'payment_app'


urlpatterns = [
    path('checkout/', views.Checkout, name='checkout'),
    path('payment/', views.Make_Payment, name='payment'), 
    path('payment-complate/', views.Complate, name='complate'),
    path('purchase/<val_id>/<tran_id>/', views.Purchas, name='purchas'),
    path('orders/', views.Order_view, name='orders'),
    path('Cencel-order/<int:id>/', views.Order_cencel, name='order_cencel')
]
