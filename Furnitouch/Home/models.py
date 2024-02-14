from django.db import models

# Create your models here.




class Home_banner(models.Model):
    offer_name = models.CharField(max_length=30)
    product_name = models.CharField(max_length=50)
    offer_banner = models.ImageField(upload_to='bannerImage')
    starting_price = models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.offer_name
    
class ProductPageBanner(models.Model):
    banner_pic = models.ImageField(upload_to='banner')
    created_at = models.DateField(auto_now_add=True)