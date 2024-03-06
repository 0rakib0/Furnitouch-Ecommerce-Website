from django.db import models
from Shop_app.models import Product
from Accounts.models import User
import random
# Create your models here.


class Shoping_Card(models.Model):
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity  = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.quantity) +'X'+str(self.product.product_name)
    

    # def save(self, *args, **kwargs):
    #     if self.product.dic_price == 0:
    #         self.total = int(self.product.main_price)*int(self.quantity)
    #     else:
    #         self.total = int(self.product.dic_price)*int(self.quantity)
    #     return super(Shoping_Card, self).save(*args, **kwargs)


    def get_total(self):
        if self.product.dic_price == 0:
            total = self.product.main_price * self.quantity
        else:
            total = self.product.dic_price * self.quantity

        float_total = format(total, '0.2f')
        return float_total

    
class Order(models.Model):
    order_item = models.ManyToManyField(Shoping_Card)
    order_num  = models.CharField(max_length=10, unique=True, blank=True, null=True)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered    = models.BooleanField(default=False)
    delivered  = models.BooleanField(default=False)
    cancel     = models.BooleanField(default=False)
    create_at  = models.DateTimeField(auto_now_add=True)
    pymentID   = models.CharField(max_length=264, blank=True, null=True)
    OrderID    = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self) -> str:
        return str(self.user.email)+"'s order"
    
    def save(self, *args, **kwargs):
        self.order_num = random.randint(1,1000000)       
        super(Order, self).save(*args, **kwargs)

    def get_totals(self):
        total = 0
        for order_Item in self.order_item.all():
            total += float(order_Item.get_total())
        return total
    
    
class OrderTraking(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    OrderTrack = models.CharField(max_length=156, default='Proccesing')
    
    def __str__(self) -> str:
        return str(self.orderId.order_num)
    
    