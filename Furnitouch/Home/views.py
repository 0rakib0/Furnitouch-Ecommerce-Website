from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Shop_app.models import Category, SubCategory, Main_Category
# Create your views here.


# @login_required
def Home(request):
    main_category = Main_Category.objects.all()
    category = Category.objects.all()
    cub_category = SubCategory.objects.all()
    context = {
        'category':category,
        'cub_category':cub_category,
        'main_category':main_category
    }
    return render(request, 'Home/home.html', context)

