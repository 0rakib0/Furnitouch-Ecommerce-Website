from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def Account(request):
    return render(request, 'accounts/register.html')


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
            messages.success(request, 'Your Account Successfylly Created!')
            return redirect('accounts:accounts')
 
    return redirect('accounts:accounts')
    


def User_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home:home')
        else:
            messages.error(request, 'Email or password not valid!')
            return redirect('accounts:register')
    return redirect('accounts:accounts')   

def User_logout(request):
    logout(request)
    return redirect('Home:home')


def Profile(request):
    return render(request, 'accounts/profile.html')