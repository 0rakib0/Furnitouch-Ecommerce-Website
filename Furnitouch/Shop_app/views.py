from django.shortcuts import render, redirect
from .models import Product, Category, SubCategory, Main_Category, WishList, ProductReview
from django.contrib.auth.decorators import login_required
from Home.models import ProductPageBanner
from Order_App.models import Shoping_Card, Order
from django.template import TemplateDoesNotExist
from django.contrib import messages
from .models import ProductMoreImage
from django.db.models import Q
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
# Create your views here.


def Shop_page(request):
    product = None
    if request.method == "GET":
        sort_value = request.GET.get('sort-value')
    main_category = request.GET.get('main-category')
    category_id = request.GET.get('category')

    
    
    product_query = Product.objects.select_related('product_main_category', 'product_category')
   
    

    if main_category !=None:
        product = product_query.filter(product_main_category__slug=main_category)
    elif category_id !=None:
        product = product_query.filter(product_category__slug=category_id)
    elif sort_value == 'a-z':
        product = product_query.all().order_by('roduct_title')
    elif sort_value == 'z-a':
        product = product_query.all().order_by('-roduct_title')
    else:
        product = product_query.all().order_by('-id')
    

    main_category = Main_Category.objects.all()
    category = Category.objects.all()
    banner = ProductPageBanner.objects.all()
    
    print(banner)
    context = {
        'category':category,
        'main_category':main_category,
        'product':product,
        'banner':banner
    }
    return render(request, 'shop_app/products.html', context)

def Single_Product(request, slug):
    user = request.user   
    save_money = None
    main_category = Main_Category.objects.all()
    category = Category.objects.all()
    releted_product = Product.objects.filter()
    product = get_object_or_404(Product, slug=slug)
    
    
    if request.method == 'POST':
        if user.is_authenticated:
            name = request.POST.get('name')
            review = request.POST.get('review')
            rating = request.POST.get('rating')
            if rating == None or rating == '':
                messages.warning(request, 'Rating value is requerd!')
                return redirect('Shop_app:single_product', slug=slug)
            
            review = ProductReview(
                productId = product,
                userId = user,
                ClientName = name,
                reviewMsg = review,
                rating = rating
            )
            
            review.save()
            messages.success(request, 'Review Successfully submit!')
            return redirect('Shop_app:single_product', slug=slug)
        else:
            messages.success(request, 'Befor Submit Review Please Login!')
            return redirect('Shop_app:single_product', slug=slug)
        
    

    product_main_price = product.main_price
    product_discount_price = product.dic_price
    if product_discount_price !=0:
        diffrent_price = product_main_price-product_discount_price
        save_money = round((diffrent_price / product_main_price) * 100)
    
    productImages = ProductMoreImage.objects.filter(product=product.id)
    category_id = product.product_category.id
    releted_product = Product.objects.filter(product_category=category_id).order_by('-id')
    releted_product_count = Product.objects.filter(product_category=category_id).count()
    
    reviews = ProductReview.objects.filter(Q(productId=product) & Q(reviewStatus=True))
    

    context = {
        'category':category,
        'main_category':main_category,
        'product':product,
        'productImages':productImages,
        'releted_product':releted_product,
        'releted_product_count':releted_product_count,
        'save_money':save_money,
        'reviews':reviews
    }
    return render(request, 'shop_app/single_products.html', context)


# -------------------> Wish List <-------------------------

@login_required
def Add_Widhlist(request, slug):
    product = Product.objects.get(slug=slug)
    user = request.user

    try:
        if WishList.objects.filter(product=product, user=user).first():
            messages.warning(request, 'This Product Already In Your Wish List')
            return redirect('Shop_app:wishlist')
        else:
            wishList = WishList(
                product = product,
                user = user
            )
            wishList.save()
            return redirect('Shop_app:wishlist')
    except TemplateDoesNotExist:
        pass


@login_required
def Wish_list(request):
    main_category = Main_Category.objects.all()
    category = Category.objects.all()
    cub_category = SubCategory.objects.all()
    wishlist = WishList.objects.filter(user=request.user)
    context = {
        'category':category,
        'cub_category':cub_category,
        'main_category':main_category,
        'wishlist':wishlist,
    }
    return render(request, 'shop_app/wishlist.html', context)

@login_required
def Remove_Wish_List(request, id):
    print(id)
    wishList = WishList.objects.get(id=id, user=request.user)
    wishList.delete()
    return redirect('Shop_app:wishlist')



# ----------------------> Card Section <------------------------
@login_required
def Shopping_Card(request):
    main_category = Main_Category.objects.all()
    category = Category.objects.all()
    cub_category = SubCategory.objects.all()
    shop_card = Shoping_Card.objects.filter(user=request.user, purchased=False)
    order = Order.objects.filter(user=request.user, ordered=False)
    if shop_card.exists() and order.exists():
        orders = order[0]
        context = {
            'category':category,
            'cub_category':cub_category,
            'main_category':main_category,
            'shop_card':shop_card,
            'orders':orders,
        }
        return render(request, 'shop_app/shoping_card.html', context)
    else:
        messages.warning(request, "You don't have any item in your cart!")
        return redirect('Home:home')


# @login_required
# def Add_product_card(request, slug):
#     user = request.user
#     product = Product.objects.get(slug=slug)
#     if Shoping_Card.objects.filter(product=product, user=user).first():
#         messages.warning(request, 'Thik Item Already Add Your Card')
#         return redirect('Shop_app:shoping_card')
#     if request.method == 'GET':
#         quantity = request.GET.get('quantity')
#         shoping_card = Shoping_Card(
#             user = user,
#             product = product,
#         )
#         if quantity:
#             shoping_card.quantity = quantity
#         shoping_card.save()
#         messages.success(request, 'Item successfully add to your card!')
#     return redirect('Shop_app:shoping_card')



# @login_required
# def Remove_Product_from_Card(request, id):
#     shop_card = Shoping_Card.objects.get(id=id, user=request.user)
#     shop_card.delete()
#     messages.success(request, 'Item successfully remove')
#     return redirect('Shop_app:shoping_card')

# def Increas_quintity(request, id):
#     product = Product.objects.get(id=id)
#     shop_card = Shoping_Card.objects.filter(user=request.user)
#     quintity = shop_card.quantity
#     print(quintity)
#     # if product:
#     #     quintity = int(product.quantity)+1
#     #     quintity.save()
#     #     messages.success(request, 'Quantity Increased!')
#     #     return redirect('Shop_app:shoping_card')
#     # else:
#     #     messages.error(request, 'Quantity Not Increase')
#     #     return redirect('Shop_app:shoping_card')
