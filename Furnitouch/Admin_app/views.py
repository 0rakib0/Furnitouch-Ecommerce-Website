from django.shortcuts import render, redirect
from Shop_app.models import Main_Category, Category, SubCategory, Product, ProductMoreImage, ProductReview
from Order_App.models import Order, OrderTraking
from Accounts.models import User, Profile
from Home.models import Home_banner, ProductPageBanner
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from datetime import datetime, timedelta, date
from Payment_app.models import Billing_address
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.



def is_admin_Check(request):
    user = request.user
    user_type = user.user_type
    print(user_type)
    if user_type != 'Admin':
        return False
    else:
        return True
    
def is_admin_Staff_Check(request):
    user = request.user
    user_type = user.user_type
    print(user_type)
    if user_type not in ['Admin', 'Staff']:
        return False
    else:
        return True



@login_required
def Admin_dashbord(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    total_order = Order.objects.filter(ordered=True)
    order_total_revinue = round(sum(order.get_totals() for order in total_order))
    order_count = total_order.count()
    total_product = Product.objects.all().count()
    total_customar = User.objects.filter(user_type='Customer').count()
    currentTime = datetime.now()
    today_date = date.today()
    Todays = Order.objects.filter(create_at__date=today_date , ordered=True)
    saven_days_ago = currentTime - timedelta(days=7)
    Last_seven_days = Order.objects.filter(Q(create_at__gte=saven_days_ago) & Q(ordered=True))
    
    context = {
        'order_count':order_count,
        'order_total_revinue':order_total_revinue,
        'total_product':total_product,
        'total_customar':total_customar,
        'Last_seven_days':Last_seven_days,
        'Todays':Todays
    }
    return render(request, 'admin_app/admin_dashbord/dashbord.html', context)

@login_required
def Add_Staff(request):
    if not is_admin_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        profile_pic = request.FILES.get('profile_pic')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Password Not Match!')
            return redirect('Admin_app:add_staff')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User Already Exist With This Email!')
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
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    user_staff = User.objects.filter(user_type='Staff')
    context = {
        'user_staff':user_staff
    }
    return render(request, 'admin_app/admin_dashbord/staff_list.html', context)

@login_required
def View_user_info(request, id):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    profile = Profile.objects.get(id=id)
    context = {
        'profile':profile
    }
    return render(request, 'admin_app/admin_dashbord/user_details.html', context)

@login_required
def Delete_user(request, id):
    if not is_admin_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    user = User.objects.get(profile=id)
    user.delete()
    messages.success(request, 'User Successfully Deleted!')
    return redirect('Admin_app:staff_list')
    


# =====================> Product Section <============================

@login_required
def Add_New_Product(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    main_category = Main_Category.objects.all().order_by('-id')
    category = Category.objects.all().order_by('-id')
    try:
        if request.method == 'POST':
            productName = request.POST.get('product_name')
            productTitle = request.POST.get('product_title')
            productImage = request.FILES.get('product_image')
            productMoreImages = request.FILES.getlist('product_more_image')
            videoId = request.POST.get('video_id')
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
                dic_price = discountPrice,
                product_video_id = videoId
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
            
            if productMoreImages != None:
                for image in productMoreImages:
                    moreImage = ProductMoreImage(
                        product = newProduct,
                        images = image
                    )
                    moreImage.save()
            messages.success(request, 'Product Successfully Added')
            return redirect('Admin_app:add_product')
    except:
        messages.success(request, 'Product info not save! something wrong!')
        return redirect('Admin_app:add_product')
    
        
    context = {
        'main_category':main_category,
        'category':category,
    }
    return render(request,'admin_app/admin_dashbord/add_product.html' , context)

@login_required
def UpdateProduct(request, slug):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    product_object = Product.objects.get(slug=slug)
    mainCate = Main_Category.objects.all()
    Categoryy = Category.objects.all()
    
    if request.method == 'POST':
        productName = request.POST.get('product_name')
        productTitle = request.POST.get('product_title')
        productImage = request.FILES.get('product_image')
        videoId = request.POST.get('videoId')
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
        print('-----------------Hello--------------')
        
        productMainCatID = Main_Category.objects.get(id=mainCategory)
        productCatID = Category.objects.get(id=productCategory)
        print(mainCategory)
        print(productCategory)
        print(productMainCatID)
        print(productCatID)
        
        product_object.product_name = productName
        product_object.product_code = productCode
        product_object.product_quintity = productQuentity
        product_object.product_main_category = productMainCatID
        product_object.product_category = productCatID
        product_object.roduct_title = productTitle
        product_object.product_keyword = productKeywords
        product_object.product_Colors = productColors
        product_object.details = productDetails
        product_object.fabrics_details = productFabrics
        product_object.Meterials_details = productMeterials
        product_object.lenth = productLenght
        product_object.deepth = productDepth
        product_object.height = productHeight
        product_object.main_price = regularPrice
        product_object.dic_price = discountPrice
        product_object.product_video_id = videoId
        
        if productImage != None:
            product_object.image = productImage
        
        if isNew:
            product_object.is_newarival = True
        if isFeatured:
            product_object.is_featured = True
        if isDiscount:
            product_object.is_discount = True
        if isReady:
            product_object.is_ready_Stock = True
            
        product_object.save()
        messages.success(request, 'Product Successfully Update')
        return redirect('Admin_app:product_list')
    context = {
        'product_object':product_object,
        'mainCate':mainCate,
        'Categoryy':Categoryy
    }
    return render(request, 'admin_app/admin_dashbord/updateProduct.html', context)

@login_required
def DeleteProduct(request, slug):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    print('------------------Delete Request Send-------------------')
    product = Product.objects.get(slug=slug)
    if product:
        product.delete()
        messages.success(request, 'Product Successfully deleted!')
        return redirect('Admin_app:product_list')
    else:
        messages.success(request, 'Product Not Delete, Something wrong!')
        return redirect('Admin_app:product_list')

@login_required
def ProductList(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    products = Product.objects.all().order_by('-id')
    
    context = {
        'products':products
    }
    
    return render(request, 'admin_app/admin_dashbord/productList.html', context)



# =====================> Category Section <============================

@login_required
def Add_main_category(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
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
        messages.success(request, 'Category not save! something wrong!')
        return redirect('Admin_app:add_main_category')
        
    return render(request, 'admin_app/admin_dashbord/add_main_category.html', context={})

@login_required
def View_main_cat(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    main_cat = Main_Category.objects.all().order_by('-id')
    context = {
        'main_cat':main_cat
    }
    return render(request, 'admin_app/admin_dashbord/view_main_cat.html', context)



@login_required
def Update_main_cat(request, slug):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
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
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    main_cat = Main_Category.objects.get(slug=slug)
    main_cat.delete()
    messages.success(request, 'Category Removed!')
    return redirect('Admin_app:view_main_cat')



@login_required
def Add_category(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    if request.method == 'POST':
        cat_name = request.POST.get('name')
        category_pic = request.FILES.get('category_pic')
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
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    cat_list = Category.objects.all().order_by('-id')
    context = {
        'cat_list':cat_list
    }
    return render(request, 'admin_app/admin_dashbord/view_category.html', context)





@login_required
def Update_cat(request, slug):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    instant_cat = Category.objects.get(slug=slug)
    if request.method == 'POST':
        cat_name = request.POST.get('name')
        cat_pic = request.FILES.get('image')
        instant_cat.category_name = cat_name
        if cat_pic != None:
            instant_cat.category_image = cat_pic
        instant_cat.save()
        messages.success(request, 'Successfully Updated!')
        return redirect('Admin_app:view_category')
    context = {
        'instant_cat':instant_cat
    }
    return render(request, 'admin_app/admin_dashbord/update_cat.html', context)





@login_required
def Del_cat(request, slug):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
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
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
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
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    sub_cat_list = SubCategory.objects.all().order_by('-id')
    print(sub_cat_list)
    context = {
        'sub_cat_list':sub_cat_list        
    }
    
    return render(request, 'admin_app/admin_dashbord/view_sub_cat.html', context)


@login_required
def Update_sub_cat(request, slug):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
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
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    sub_cat = SubCategory.objects.get(slug=slug)
    if sub_cat:
        sub_cat.delete()
        messages.success(request, 'Sub Category Successfully Deleted!')
        return redirect('Admin_app:view_sub_cat')
    else:
        messages.error(request, 'Not Deleted, Something wrong!')
        return redirect('Admin_app:view_sub_cat')

# =====================================> Baner <===================================
@login_required
def HomePageBenner(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
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
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    home_banner = Home_banner.objects.all().order_by('-id')
    context = {
        'home_banner':home_banner
    }
    return render(request, 'admin_app/admin_dashbord/banner_list.html', context)

@login_required
def Delete_banner(request, id):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    banner = Home_banner.objects.get(id=id)
    if banner:
        banner.delete()
        messages.success(request, 'Banner Removed!')
        return redirect('Admin_app:banner_list')
    else:
        messages.success(request, 'Banner Remove Fail!')
        return redirect('Admin_app:banner_list')
    
def ProductPageBannerr(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
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
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    pending_order_list = Order.objects.filter(delivered=False, ordered=True).order_by('-id')
    context = {
        'pending_order_list':pending_order_list
    }
    return render(request, 'admin_app/admin_dashbord/pending_order_list.html', context)

@login_required
def Delivered_order_list(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    delivered_order_list = Order.objects.filter(delivered=True).order_by('-id')
    context = {
        'delivered_order_list':delivered_order_list
    }
    return render(request, 'admin_app/admin_dashbord/delivered_order_list.html', context)



@login_required
def Order_details(request, id):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    order_ditails = Order.objects.get(id=id, ordered=True)
    user = order_ditails.user
    order_shiping_address = Billing_address.objects.get(user=user)
    print(order_shiping_address)    
    if order_ditails:
        context = {
            'order_ditails':order_ditails,
            'order_shiping_address':order_shiping_address
        }
        return render(request, 'admin_app/admin_dashbord/order_details.html', context)
    else:
        messages.success(request, 'No Item Found. Something wrong!')
        return redirect('Admin_app:pending_order_list')
    

@login_required
def Order_delivery(request, id):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    delivery_order = Order.objects.get(id=id, ordered=True)
    if delivery_order:
        delivery_order.delivered = True
        delivery_order.save()
        messages.success(request, 'Order Successfully Deliered!')
        return redirect('Admin_app:pending_order_list')
    else:
        messages.success(request, 'Order Not Deliered!')
        return redirect('Admin_app:pending_order_list')
    
    
    
# -----------------------------> Customar Report <-------------------------------
@login_required
def CustomarList(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    Customar = User.objects.filter(user_type='Customer')
    print(Customar)
    context = {
        'Customar':Customar
    }
    return render(request, 'admin_app/admin_dashbord/Customars.html', context)


# -------------------------------> Sales Report <----------------------------------

@login_required
def SalesReport(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    currentTime = datetime.now()
    saven_days_ago = currentTime - timedelta(days=7)
    one_month_ago = currentTime - timedelta(days=30)
    six_month_ago = currentTime - timedelta(days=6*30)
    one_year_ago = currentTime - timedelta(days=365)
    
    
    sortValue = request.GET.get('sort-value')
    if sortValue == 'last-week-report':
        orderObj = Order.objects.filter(Q(create_at__gte=saven_days_ago) & Q(ordered=True))
    elif sortValue == 'last-mont-report':
        orderObj = Order.objects.filter(Q(create_at__gte=one_month_ago) & Q(ordered=True))
    elif sortValue == 'last-6mont-report':
        orderObj = Order.objects.filter(Q(create_at__gte=six_month_ago) & Q(ordered=True))  
    elif sortValue == 'last-year-report':
        orderObj = Order.objects.filter(Q(create_at__gte=one_year_ago) & Q(ordered=True))
    else:
        orderObj = Order.objects.filter(ordered=True)
    context = {
        "orderObj":orderObj
    }
    return render(request, 'admin_app/admin_dashbord/saleReport.html', context)


# ------------------------------> Order Tracking <----------------------------
@login_required
def TrackOrder(request, Orderid=None):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    orderTrakingList = OrderTraking.objects.all()
    context = {
        'orderTrakingList':orderTrakingList
    }
    return render(request, 'admin_app/admin_dashbord/orderTrack.html', context)

@login_required    
def AddTrackingOrder(request, Orderid):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    order = Order.objects.get(id=Orderid)
    user = order.user
    try:
        in_track = OrderTraking.objects.get(orderId=order)
        if in_track:
            return redirect('Admin_app:track_order')
    except ObjectDoesNotExist:
        track = OrderTraking (
            orderId = order,
            user = user
        )
        track.save()
        messages.success(request, f'{order.order_num} No Order Start Tracking')
        return redirect('Admin_app:track_order')
    
    
@login_required
def trakingDelete(request, id):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    orderTrack = OrderTraking.objects.get(id=id)
    orderTrack.delete()    
    messages.success(request, 'Successfully Deleted')
    return redirect('Admin_app:track_order')


@login_required
def TrackingUpdate(request, id):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    traking_status = None
    trakingId = OrderTraking.objects.get(id=id)
    
    if request.method == 'POST':
        traking_status = request.POST.get('traking')
        if traking_status != None or traking_status != '':
            trakingId.OrderTrack=traking_status
            trakingId.save()
            messages.success(request, f"{trakingId.orderId.order_num} No Order Traking Update")
            return redirect('Admin_app:track_order')
    context = {
        'trakingId':trakingId
    }
    return render(request, 'admin_app/admin_dashbord/OrderTrackUpdate.html', context)


# ------------------------------> Product Review <-------------------------------
@login_required
def Reviews(request):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    product_review = ProductReview.objects.all().order_by('-id')
    print(product_review)
    context = {
        "product_review":product_review
    }
    return render(request, 'admin_app/admin_dashbord/ProductReviewList.html', context)

@login_required
def ReviewApprove(request, id):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    review = ProductReview.objects.get(id=id)
    if review:
        review.reviewStatus = True
        review.save()
        messages.success(request, 'Review Succeefully Approved!')
        return redirect('Admin_app:product_review')
    else:
        messages.success(request, 'Review Not Approved, Something Wrong!')
        return redirect('Admin_app:product_review')

@login_required
def DeleteReview(request, id):
    if not is_admin_Staff_Check(request):
        messages.warning(request, 'You Are Not Allowed For This Access!')
        return redirect('accounts:logout')
    review = ProductReview.objects.get(id=id)
    if review:
        review.delete()
        messages.success(request, 'Review Succeefully Deleted!')
        return redirect('Admin_app:product_review')
    else:
        messages.success(request, 'Review Not Delete, Something Wrong!')
        return redirect('Admin_app:product_review')



    