from django.shortcuts import render
from .models import User
# Create your views here.

def Regitration(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(email, password1, password2)

        
    
    return render(request, 'accounts/register.html')
