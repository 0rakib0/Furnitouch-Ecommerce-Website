from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def Regitration(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(email=email).first():
            messages.warning(request, 'Email Already exist!')
            return redirect('accounts:register')
        if password1 != password2:
            messages.warning(request, 'Password not match!')
            return redirect('accounts:register')
        else:  
            mk_pass = make_password(password1)
            user = User (
                email = email,
                password = mk_pass
            )
            user.save()
            messages.success(request, 'Account successfully created!')
            return redirect('accounts:register')
    return render(request, 'accounts/register.html')


def User_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # password = check_password(password, password)
        
        user = User.objects.get(email=email)
        if user:
            if check_password(password, user.password):
                return redirect('Home:home')
        else:
            messages.error(request, 'Email and password Not match!')
            return redirect('accounts:register')
       
        # user = authenticate(email=email, password=check_password(password, password))
        # if user:
        #     login(request, user)
        #     return redirect('Home:home')
        # else:
        #     messages.error(request, 'Login Not success!')
        #     return redirect('accounts:register')
       
    return render(request, 'accounts/register.html')
