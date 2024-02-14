from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Shoping_Card, Order
from Shop_app.models import Product
from django.contrib import messages
# Create your views here.


def Add_to_Card(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_items = Shoping_Card.objects.get_or_create(product=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.order_item.filter(product=item).exists():
            order_items[0].quantity += 1
            order_items[0].save()
            messages.success(request, 'This item quintity was updated.')
            return redirect('Shop_app:shoping_card')
        else:
            order.order_item.add(order_items[0])
            messages.success(request, 'This Item is Added To your Card')
            return redirect('Shop_app:shoping_card')
    else:
        order = Order(user=request.user)
        order.save()
        order.order_item.add(order_items[0])
        messages.success(request, 'This item added to your card!')
        return redirect('Shop_app:shoping_card')
    

@login_required
def Remove_Product_from_Card(request, id):
    shop_card = Shoping_Card.objects.get(id=id, user=request.user, purchased=False)
    shop_card.delete()
    messages.success(request, 'Item successfully remove')
    return redirect('Shop_app:shoping_card')


@login_required
def Increse_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_item.filter(product=item).exists():
            order_item = Shoping_Card.objects.filter(product=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.success(request, 'Quantity Increased!')
                return redirect('Shop_app:shoping_card')
        else:
            messages.warning(request, 'This product is not your card!')
            return redirect('Shop_app:shop_page')

    else:
        messages.warning(request, 'You do not have an active order!')
        return redirect('Shop_app:shop_page')
    
@login_required
def Dicrease_card(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_item.filter(product=item).exists():
            order_item = Shoping_Card.objects.filter(product=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.success(request, 'Quantity Dicreased!')
                return redirect('Shop_app:shoping_card')
        else:
            messages.warning(request, 'This product is not your card!')
            return redirect('Shop_app:shop_page')

    else:
        messages.warning(request, 'You do not have an active order!')
        return redirect('Shop_app:shop_page')


