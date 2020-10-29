"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ecommerce.settings import DEBUG
from django.contrib import admin
from django.urls import path

#base views
from .views import *

#products custom app
from products.views import product_detail_behdashti, product_detail_tebi, shop , Eshop

#detail views
from products.views import product_detail_behdashti, product_detail_tebi , ProductDetail

#static config
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #main page
    path('admin/', admin.site.urls),
    path('', home),
    path('login', login),
    path('register', register),

    #shop views
    path('shop', shop),
    path('eshop', Eshop.as_view()),

    #detail views for products
    path('shop/medical/<productId>', product_detail_behdashti),
    path('shop/correctional/<productId>', product_detail_tebi),
    path('eshop/<productId>', ProductDetail.as_view()),


]

if settings.DEBUG == True :
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
