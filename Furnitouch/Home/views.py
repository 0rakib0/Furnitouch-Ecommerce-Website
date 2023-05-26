from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from Shop_app.models import Category, SubCategory, Main_Category
=======
from Accounts.models import Profile
>>>>>>> 70ec0d4ee74df07a78a6b5673480523c0dd2eee7
# Create your views here.


# @login_required
def Home(request):
<<<<<<< HEAD
    main_category = Main_Category.objects.all()
    category = Category.objects.all()
    cub_category = SubCategory.objects.all()
    context = {
        'category':category,
        'cub_category':cub_category,
        'main_category':main_category
=======
    user = request.user
    profile = None
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
    context = {
        'profile':profile,
>>>>>>> 70ec0d4ee74df07a78a6b5673480523c0dd2eee7
    }
    return render(request, 'Home/home.html', context)

