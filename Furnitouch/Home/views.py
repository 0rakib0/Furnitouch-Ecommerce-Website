from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def Home(request):
    context = {

    }

    return render(request, 'Home/home.html', context)
