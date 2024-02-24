from django.shortcuts import render, redirect
from Shop_app.models import Main_Category, Category, SubCategory, Product
from Order_App.models import Order
from Accounts.models import User, Profile
from Home.models import Home_banner, ProductPageBanner
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def Add_Staff(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        profile_pic = request.FILES.get('profile_pic')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Password Not Match!')
            return redirect('Admin_app:add_staff')
        
        user = User(
            email = email            
        )
        user.user_type = 'Staff'
        user.set_password(password1)
        user.save()
        
        use_id = User.objects.get(email=email)
        
        profile = Profile.objects.get(user=use_id)
        profile.full_name = full_name
        profile.profile_pic = profile_pic
        profile.save()
        messages.success(request, 'Staff Account successfully created!')
        return redirect('Admin_app:add_staff')
        
    return render(request, 'admin_app/admin_dashbord/add_staff.html')

@login_required
def Staff_List(request):
    user_staff = User.objects.filter(user_type='Staff')
    context = {
        'user_staff':user_staff
    }
    return render(request, 'admin_app/admin_dashbord/staff_list.html', context)

@login_required
def View_user_info(request, id):
    profile = Profile.objects.get(id=id)
    context = {
        'profile':profile
    }
    return render(request, 'admin_app/admin_dashbord/user_details.html', context)

def Delete_user(request, id):
    user = User.objects.get(profile=id)
    user.delete()
    messages.success(request, 'User Successfully Deleted!')
    return redirect('Admin_app:staff_list')
    




@login_required
def Admin_dashbord(request):
    context = {
        
    }
    return render(request, 'admin_app/admin_dashbord/dashbord.html', context)

# =====================> Product Section <============================

@login_required
def Add_New_Product(request):
    main_category = Main_Category.objects.all().order_by('-id')
    category = Category.objects.all().order_by('-id')
    # try:
    if request.method == 'POST':
        productName = request.POST.get('product_name')
        productTitle = request.POST.get('product_title')
        productImage = request.FILES.get('product_image')
        productCode = request.POST.get('product_code')
        productQuentity = request.POST.get('product_quentity')
        productColors = request.POST.get('product_colors')
        productKeywords = request.POST.get('product_keyword')
        productFabrics = request.POST.get('product_fabrics')
        productMeterials = request.POST.get('product_meterial')
        productLenght = request.POST.get('product_lenght')
        productDepth = request.POST.get('product_deepth')
        productHeight = request.POST.get('product_height')
        regularPrice = request.POST.get('regular_price')
        discountPrice = request.POST.get('discount_price')
        mainCategory = request.POST.get('main_cat')
        productCategory = request.POST.get('category')
        productDetails = request.POST.get('product_details')
        isNew = request.POST.get('is_new')
        isFeatured = request.POST.get('is_featured')
        isDiscount = request.POST.get('is_discount')
        isReady = request.POST.get('is_ready')
        
        productMainCatID = Main_Category.objects.get(id=mainCategory)
        productCatID = Category.objects.get(id=productCategory)
            
        print(isDiscount)
        print(isNew)
        print(isFeatured)
        print(isReady)
        
        if (main_category == '--SELECT--' or productCategory == '--SELECT--'):
            messages.success(request, 'Category Relect is required')
            return redirect('Admin_app:add_product')
        
        newProduct = Product(
            product_name = productName,
            product_code = productCode,
            product_quintity = productQuentity,
            product_main_category = productMainCatID,
            product_category = productCatID,
            roduct_title = productTitle,
            product_keyword = productKeywords,
            image = productImage,
            product_Colors = productColors,
            details = productDetails,
            fabrics_details = productFabrics,
            Meterials_details = productMeterials,
            lenth = productLenght,
            deepth = productDepth,
            height = productHeight,
            main_price = regularPrice,
            dic_price = discountPrice
        )
        
        if isNew:
            newProduct.is_newarival = True
        if isFeatured:
            newProduct.is_featured = True
        if isDiscount:
            newProduct.is_discount = True
        if isReady:
            newProduct.is_ready_Stock = True
        
        newProduct.save()
        messages.success(request, 'Product Successfully Added')
        return redirect('Admin_app:add_product')
    # except:
    #     messages.warning(request, 'Product info not save! something wrong!')
    #     return redirect('Admin_app:add_product')
    
        
    context = {
        'main_category':main_category,
        'category':category,
    }
    return render(request,'admin_app/admin_dashbord/add_product.html' , context)


def ProductList(request):
    products = Product.objects.all()
    
    context = {
        'products':products
    }
    
    return render(request, 'admin_app/admin_dashbord/productList.html', context)



# =====================> Category Section <============================

@login_required
def Add_main_category(request):
    try:
        if request.method == 'POST':
            category_name = request.POST.get('name')
            
            main_cat = Main_Category(
                main_category_name = category_name
            )
            main_cat.save()
            messages.success(request, 'Category suceessfully added!')
            return redirect('Admin_app:add_main_category')
        
    except:
        messages.warning(request, 'Category not save! something wrong!')
        return redirect('Admin_app:add_main_category')
        
    return render(request, 'admin_app/admin_dashbord/add_main_category.html', context={})

@login_required
def View_main_cat(request):
    main_cat = Main_Category.objects.all().order_by('-id')
    context = {
        'main_cat':main_cat
    }
    return render(request, 'admin_app/admin_dashbord/view_main_cat.html', context)
@login_required
def Update_main_cat(request, slug):
    main_cat = Main_Category.objects.get(slug=slug)
    if request.method == 'POST':
        main_cats = Main_Category.objects.get(slug=slug)
        main_cat_name = request.POST.get('name')
        main_cats.main_category_name = main_cat_name
        main_cats.save()
        messages.success(request, 'Category successfully Updated!')
        return redirect('Admin_app:view_main_cat')
        
    context = {
        'main_cat':main_cat
    }
    return render(request, 'admin_app/admin_dashbord/update_main_cat.html', context)
@login_required
def Del_main_cat(request, slug):
    main_cat = Main_Category.objects.get(slug=slug)
    main_cat.delete()
    messages.success(request, 'Category Removed!')
    return redirect('Admin_app:view_main_cat')



@login_required
def Add_category(request):
    if request.method == 'POST':
        cat_name = request.POST.get('name')
        category_pic = request.POST.get('category_pic')
        main_cat_id = request.POST.get('main_cat_id')
        if main_cat_id == '--SELECT--':
            messages.success(request, 'Main Category Must Be Select!')
            return redirect('Admin_app:add_category')
        main_cat = Main_Category.objects.get(id=main_cat_id)

        category = Category(
            category_name = cat_name,
            main_category = main_cat,
            category_image = category_pic
            
        )
        category.save()
        messages.success(request, 'Category Successfully Added')
        return redirect('Admin_app:add_category')
    
    Main_cat = Main_Category.objects.all()
    context = {
        'Main_cat':Main_cat
    }
    return render(request, 'admin_app/admin_dashbord/add_category.html', context)


@login_required
def View_Category(request):
    cat_list = Category.objects.all().order_by('-id')
    context = {
        'cat_list':cat_list
    }
    return render(request, 'admin_app/admin_dashbord/view_category.html', context)

@login_required
def Update_cat(request, slug):
    instant_cat = Category.objects.get(slug=slug)
    if request.method == 'POST':
        cat_name = request.POST.get('name')
        instant_cat.category_name = cat_name
        instant_cat.save()
        messages.success(request, 'Successfully Updated!')
        return redirect('Admin_app:view_category')
    context = {
        'instant_cat':instant_cat
    }
    return render(request, 'admin_app/admin_dashbord/update_cat.html', context)

@login_required
def Del_cat(request, slug):
    category = Category.objects.get(slug=slug)
    if category:
        category.delete()
        messages.success(request, 'Category Successfully Deleted!')
        return redirect('Admin_app:view_category')
    else:
        messages.error(request, 'Not Deleted, Something wrong!')
        return redirect('Admin_app:view_category')
    
    
@login_required   
def Add_sub_category(request):
    if request.method == 'POST':
        sub_cat_name = request.POST.get('name')
        cat_id       = request.POST.get('cat_id')
        if cat_id == '--SELECT--':
            messages.success(request, 'Category Must Be Select!')
            return redirect('Admin_app:add_sub_cat')
        category = Category.objects.get(id=cat_id)
        
        sub_cat = SubCategory(
            Category_id = category,
            sub_category_name = sub_cat_name
        )
        sub_cat.save()
        messages.success(request, 'Sub Category Successfully Added!')
        return redirect('Admin_app:add_sub_cat')
    category = Category.objects.all().order_by('-id')
    context = {
        'category':category
    }
    return render(request, 'admin_app/admin_dashbord/add_sub_cat.html', context)

@login_required
def View_sub_Cat(request):
    sub_cat_list = SubCategory.objects.all().order_by('-id')
    print(sub_cat_list)
    context = {
        'sub_cat_list':sub_cat_list        
    }
    
    return render(request, 'admin_app/admin_dashbord/view_sub_cat.html', context)


@login_required
def Update_sub_cat(request, slug):
    instant_sub_cat = SubCategory.objects.get(slug=slug)
    if request.method == 'POST':
        sub_cat_name = request.POST.get('name')
        instant_sub_cat.sub_category_name = sub_cat_name
        instant_sub_cat.save()
        messages.success(request, 'Successfully Updated!')
        return redirect('Admin_app:view_sub_cat')
    context = {
        'instant_sub_cat':instant_sub_cat
    }
    return render(request, 'admin_app/admin_dashbord/update_sub_cat.html', context)


@login_required
def Del_sub_cat(request, slug):
    sub_cat = SubCategory.objects.get(slug=slug)
    if sub_cat:
        sub_cat.delete()
        messages.success(request, 'Sub Category Successfully Deleted!')
        return redirect('Admin_app:view_sub_cat')
    else:
        messages.error(request, 'Not Deleted, Something wrong!')
        return redirect('Admin_app:view_sub_cat')

# =====================================> Baner <===================================
def HomePageBenner(request):
    if request.method == 'POST':
        offer_name = request.POST.get('offer_name')
        product_name = request.POST.get('product_name')
        banner_pic = request.FILES.get('banner_pic')
        starting_price = request.POST.get('starting_price')
        
        home_baner = Home_banner(
            offer_name = offer_name,
            product_name = product_name,
            offer_banner = banner_pic,
            starting_price = starting_price
        )
        
        home_baner.save()
        messages.success(request, 'Banner Successfully added!')
        return redirect('Admin_app:home_page_banner')
    return render(request, 'admin_app/admin_dashbord/home_page_banner.html')


@login_required
def Banner_List(request):
    home_banner = Home_banner.objects.all().order_by('-id')
    context = {
        'home_banner':home_banner
    }
    return render(request, 'admin_app/admin_dashbord/banner_list.html', context)

@login_required
def Delete_banner(request, id):
    banner = Home_banner.objects.get(id=id)
    if banner:
        banner.delete()
        messages.success(request, 'Banner Removed!')
        return redirect('Admin_app:banner_list')
    else:
        messages.success(request, 'Banner Remove Fail!')
        return redirect('Admin_app:banner_list')
    
def ProductPageBannerr(request):
    if request.method == 'POST':
        banner_pic = request.FILES.get('banner_pic')
        
        banner = ProductPageBanner.objects.get(id=2)
        banner.banner_pic = banner_pic
        banner.save()
        messages.success(request, 'New Banner Uploaded!')
        return redirect('Admin_app:product_page_banner')
    return render(request, 'admin_app/admin_dashbord/product_page_banner.html')
    
    
# ====================================== Staff Dashbord <=====================================




#=======================================> Order Details <====================================
@login_required
def Pending_Order_List(request):
    pending_order_list = Order.objects.filter(delivered=False, ordered=True).order_by('-id')
    context = {
        'pending_order_list':pending_order_list
    }
    return render(request, 'admin_app/admin_dashbord/pending_order_list.html', context)

def Delivered_order_list(request):
    delivered_order_list = Order.objects.filter(delivered=True).order_by('-id')
    context = {
        'delivered_order_list':delivered_order_list
    }
    return render(request, 'admin_app/admin_dashbord/delivered_order_list.html', context)

def Order_details(request, id):
    order_ditails = Order.objects.get(id=id, ordered=True)
    
    if order_ditails:
        context = {
            'order_ditails':order_ditails
        }
        return render(request, 'admin_app/admin_dashbord/order_details.html', context)
    else:
        messages.success(request, 'No Item Found. Something wrong!')
        return redirect('Admin_app:pending_order_list')

@login_required
def Order_delivery(request, id):
    delivery_order = Order.objects.get(id=id, ordered=True)
    if delivery_order:
        delivery_order.delivered = True
        delivery_order.save()
        messages.success(request, 'Order Successfully Deliered!')
        return redirect('Admin_app:pending_order_list')
    else:
        messages.success(request, 'Order Not Deliered!')
        return redirect('Admin_app:pending_order_list')
    
    