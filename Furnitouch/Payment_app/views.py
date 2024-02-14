from django.shortcuts import render, redirect, HttpResponseRedirect
from Order_App.models import Order, Shoping_Card
from Payment_app.models import Billing_address
from django.contrib import messages
from Accounts.models import Profile, User
from django.contrib.auth.decorators import login_required
from Shop_app.models import Category, SubCategory, Main_Category
from django.urls import reverse




# for payment
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@login_required
def Checkout(request):
    if request.method == 'POST':
        address_1 = request.POST.get('address_1')
        address_2 = request.POST.get('address_2')
        zipcode = request.POST.get('zipcode')
        city = request.POST.get('city')
        country_id = request.POST.get('country')

        country = Profile.objects.get(id=country_id)
        country = country.country

        billing_address = Billing_address.objects.get(user=request.user)
        
        billing_address.address_1 = address_1
        billing_address.address_2 = address_2
        billing_address.zipcode   = zipcode
        billing_address.city      = city
        billing_address.country   = country
        billing_address.save()
        messages.success(request, 'Billing Info Successfully save!')
        return redirect('payment_app:checkout')
    main_category = Main_Category.objects.all()
    category = Category.objects.all()
    cub_category = SubCategory.objects.all()
    profile = Profile.objects.get(user=request.user)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    order_items = order_qs[0].order_item.all()
    order_total = order_qs[0].get_totals()
    save_billing_address = Billing_address.objects.get(user=request.user)
    context = {
        'category':category,
        'cub_category':cub_category,
        'main_category':main_category,
        'profile':profile,
        'order_items':order_items,
        'order_total':order_total,
        'save_billing_address':save_billing_address
    }
    return render(request, 'Payment_app/checkout.html', context)


@login_required
def Make_Payment(request):
    save_adress = Billing_address.objects.get(user=request.user)
    if not save_adress.is_fully_filled():
        messages.warning(request, 'Please complate shipping address!')
        return redirect('payment_app:checkout')

    if not request.user.profile.is_fully_filed():
        messages.warning(request, 'Please complate profile details!')
        return redirect('accounts:profile')
    
    stor_id = 'furni64836bd635daa'
    API_Key = 'furni64836bd635daa@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=stor_id, sslc_store_pass=API_Key)

    status_url = request.build_absolute_uri(reverse('payment_app:complate'))
    

    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)


    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].order_item.all()
    order_item_count = order_qs[0].order_item.count()
    order_total = order_qs[0].get_totals()

    

    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='Mixed', product_name=order_items, num_of_item=order_item_count, shipping_method='pichup', product_profile='None')


    corrent_user = request.user


    mypayment.set_customer_info(name=corrent_user.profile.full_name, email=corrent_user.email, address1=corrent_user.profile.address_1, address2=corrent_user.profile.address_1, city=corrent_user.profile.city, postcode=corrent_user.profile.zipcode, country=corrent_user.profile.country, phone=corrent_user.profile.phone)

    mypayment.set_shipping_info(shipping_to=corrent_user.profile.full_name, address=save_adress.address_1, city=save_adress.city, postcode=save_adress.zipcode, country=save_adress.country)

    response_data = mypayment.init_payment()
    return redirect(response_data['GatewayPageURL'])



@csrf_exempt
def Complate(request):
    if request.method == 'POST' or 'post':
        payment_data = request.POST
    
        status = (payment_data['status'])
        

        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request, 'Your Paymant Complate Successfully! page will be redirected!')
            return HttpResponseRedirect(reverse('payment_app:purchas', kwargs={'tran_id':tran_id, 'val_id':val_id},))

        if status == 'FAILED':
            messages.warning(request, 'Your Payment Faild! Please Try Again! page will be redirected! ')

    return render(request, 'Payment_app/complate.html')


@login_required
def Purchas(request, val_id, tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    orderId = val_id

    order.ordered = True
    order.OrderID = orderId
    order.pymentID = tran_id
    order.save()

    cart_iteams = Shoping_Card.objects.filter(user=request.user, purchased=False)
    for i in cart_iteams:
        i.purchased=True
        i.save()
    return HttpResponseRedirect(reverse('Home:home'))

@login_required
def Order_view(request):
    try:
        orders = Order.objects.filter(user=request.user, ordered=True)
       
        context = {'orders':orders}
    except:
        messages.warning(request, 'You do not have an active order!')
        return redirect('Home:home')
    return render(request, 'Payment_app/order.html', context)

@login_required
def Order_cencel(request, id):
    Order_cencel = Order.objects.get(id=id, ordered=True)
    if Order_cencel:
        Order_cencel.cancel = True
        Order_cencel.save()
        messages.success(request,'Order Cenceled!')
        return redirect('payment_app:orders')
    else:
        messages.success(request,'Order Not Cencel! Something Wrong!')
        return redirect('payment_app:orders')