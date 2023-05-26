from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Main_Category(models.Model):
    main_category_name = models.CharField(max_length=150)
    slug               = models.SlugField(unique=True, null=True, blank=True)
    

    def __str__(self) -> str:
        return self.main_category_name



class Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE, related_name='main_cat')
    category_name       = models.CharField(max_length=100)
    description         = models.CharField(max_length=250)
    slug                = models.SlugField(unique=True, null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.category_name
    

class SubCategory(models.Model):
    Category_id           = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat')
    sub_category_name     = models.CharField(max_length=100)
    description           = models.CharField(max_length=250)
    slug                  = models.SlugField(unique=True, null=True, blank=True)
    created_at            = models.DateTimeField(auto_now_add=True)
    updated_at            = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return self.sub_category_name


class Product(models.Model):
    product_name         = models.CharField(max_length=260)
    product_main_category= models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    product_category     = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    product_sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    roduct_title         = models.CharField(max_length=260)
    product_description  = models.TextField()
    product_keyword      = models.CharField(max_length=150, blank=True, null=True)
    image                = models.ImageField(upload_to='products')
    slug                 = models.SlugField(unique=True, null=True, blank=True)
    details              = models.TextField()
    main_price           = models.IntegerField()
    is_discount          = models.BooleanField(default=False)
    dic_price            = models.IntegerField(default=0, blank=True, null=True)
    cerated_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.product_name