from django.db import models
import uuid
from Accounts.models import User
from django.utils.text import slugify

# Create your models here.

class Main_Category(models.Model):
    main_category_name = models.CharField(max_length=150)
    created_at         = models.DateField(auto_now_add=True)
    slug               = models.SlugField(unique=True, null=True, blank=True)
    

    def __str__(self) -> str:
        return self.main_category_name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.main_category_name)+'-'+ str(uuid.uuid4())
        
        return super(Main_Category, self).save(*args, **kwargs)



class Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE, related_name='main_cat')
    category_name       = models.CharField(max_length=100)
    category_image      = models.ImageField(upload_to='category_Pic')
    slug                = models.SlugField(unique=True, null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.category_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)+'-'+ str(uuid.uuid4())
        
        return super(Category, self).save(*args, **kwargs)
    

class SubCategory(models.Model):
    Category_id           = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat')
    sub_category_name     = models.CharField(max_length=100)
    slug                  = models.SlugField(unique=True, null=True, blank=True)
    created_at            = models.DateTimeField(auto_now_add=True)
    updated_at            = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return self.sub_category_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.sub_category_name)+'-'+ str(uuid.uuid4())
        
        return super(SubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    product_name         = models.CharField(max_length=260)
    product_code         = models.CharField(max_length=20)
    product_quintity     = models.IntegerField(default=0)
    product_main_category= models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    product_category     = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    roduct_title         = models.CharField(max_length=260)
    product_keyword      = models.CharField(max_length=150, blank=True, null=True)
    image                = models.ImageField(upload_to='products')
    thumbnail_pic        = models.ImageField(upload_to='products')
    product_video_id     = models.CharField(max_length=250)
    slug                 = models.SlugField(unique=True, null=True, blank=True)
    product_Colors       = models.CharField(max_length=256)
    details              = models.TextField()
    fabrics_details      = models.CharField(max_length=165, blank=True, null=True)
    Meterials_details         = models.CharField(max_length=165)
    lenth                = models.CharField(max_length=30)
    deepth                = models.CharField(max_length=30)
    height               = models.CharField(max_length=30)
    main_price           = models.IntegerField()
    is_newarival         = models.BooleanField(default=False)
    is_featured          = models.BooleanField(default=False)
    is_discount          = models.BooleanField(default=False)
    is_ready_Stock       = models.BooleanField(default=False)
    dic_price            = models.IntegerField(default=0, blank=True, null=True)
    cerated_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.product_name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.roduct_title)+'-'+ str(uuid.uuid4())
        
        return super(Product, self).save(*args, **kwargs)
    
    
class ProductMoreImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pro_mul_ing', null=True, blank=True)
    images = models.ImageField(upload_to='products', null=True, blank=True)
    
    
    def __str__(self) -> str:
        return str(self.product.product_name) + "'s Images"
    
  
class WishList(models.Model):
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.user.email) +'==>'+str(self.product.product_name)
    
    
    
class ProductReview(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ClientName = models.CharField(max_length=156)
    reviewMsg = models.TextField()
    rating = models.IntegerField(default=4)
    reviewStatus = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.productId.product_name)  +"'s Review"
    
    

