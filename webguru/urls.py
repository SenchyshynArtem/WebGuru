"""webguru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL
from userpage.views import *
from basket.views import *
from catalogue.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", show_main, name='main'),
    path("about_us/", show_about_us, name='about_us'),
    path("basket/", show_basket, name='basket'),
    path("catalogue/", show_catalogue, name='catalogue'),
    path("product/<product_pk>", show_product, name='product'),
    path("delete_from_basket/", delete_from_basket, name='delete_from_basket'),
    path("order_processing/", order_processing, name='order_processing'),
    path("feedback_success/", feedback_success, name='feedback_success'),
]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
