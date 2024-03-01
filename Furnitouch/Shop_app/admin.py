from django.contrib import admin
from .models import Category, SubCategory, Product, Main_Category, WishList, ProductMoreImage, ProductReview
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Main_Category)
admin.site.register(WishList)
admin.site.register(ProductMoreImage)
admin.site.register(ProductReview)