from django.shortcuts import render
from .models import Product, Category, SubCategory, Main_Category
# Create your views here.


def Shop_page(request):
    main_category = Main_Category.objects.all()
    category = Category.objects.all()
    cub_category = SubCategory.objects.all()
    product = Product.objects.all().order_by('-id')
    context = {
        'category':category,
        'cub_category':cub_category,
        'main_category':main_category,
        'product':product,
    }
    return render(request, 'shop_app/products.html', context)
