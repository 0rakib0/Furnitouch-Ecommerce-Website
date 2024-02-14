from django import template
from Order_App.models import Shoping_Card
from Shop_app.models import WishList

register = template.Library()


@register.filter
def cart_total(user):
    cart_items = Shoping_Card.objects.filter(user=user, purchased=False)

    if cart_items.exists():
        return cart_items.count()
    else:
        return 0
    
@register.filter
def wishlist_total(user):
    wishlist = WishList.objects.filter(user=user)

    if wishlist.exists():
        return wishlist.count()
    else:
        return 0