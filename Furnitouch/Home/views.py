from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Order_App.models import Shoping_Card
from Accounts.models import Profile
from Shop_app.models import Product
from .models import Home_banner
from Shop_app.models import Category, SubCategory, Main_Category, WishList
from django.db.models import Q

# Create your views here.


# @login_required
def Home(request):
    profile = None
    main_category = Main_Category.objects.all()
    category = Category.objects.all()[:12]
    cub_category = SubCategory.objects.all()
    if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
    new_product = Product.objects.filter(is_newarival=True).order_by('-id')[:5]
    banner_info = Home_banner.objects.all().order_by('-id')
    bedCatId = Category.objects.get(category_name="Bed")
    sofaCatId = Category.objects.get(category_name="Sofa")
    bedRoomatId = Category.objects.get(category_name='Bedroom Set')
    featursBed = Product.objects.filter(Q(product_category=bedCatId) & Q(is_featured=True))
    featursSofa = Product.objects.filter(Q(product_category=sofaCatId) & Q(is_featured=True))
    featursBerroom = Product.objects.filter(Q(product_category=bedRoomatId) & Q(is_featured=True))
    
    context = {
        'category':category,
        'cub_category':cub_category,
        'main_category':main_category,
        'profile':profile,
        'new_product':new_product,
        'banner_info':banner_info,
        'featursBed':featursBed,
        'featursSofa':featursSofa,
        'featursBerroom':featursBerroom
    }
    return render(request, 'Home/home.html', context)

def New_Product(request):
    new_product = Product.objects.filter(is_newarival=True)
    context = {
        'new_product':new_product
    }
    return render(request, 'shop_app/new_product.html', context)

