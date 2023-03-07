from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Accounts.models import Profile
# Create your views here.


# @login_required
def Home(request):
    user = request.user
    profile = None
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
    context = {
        'profile':profile,
    }

    return render(request, 'Home/home.html', context)
