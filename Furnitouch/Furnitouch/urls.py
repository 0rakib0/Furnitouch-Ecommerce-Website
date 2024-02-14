from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('Accounts.urls')),
    path('', include('Shop_app.urls')),
    path('', include('Order_App.urls')),
    path('', include('Payment_app.urls')),
    path('', include('Admin_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

