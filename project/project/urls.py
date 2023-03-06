"""project URL Configuration

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
from django.contrib.auth.views import LoginView, LogoutView
from django.template.context_processors import media
from django.urls import path
from django.urls.conf import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from orders.views import main_page
from orders.api import api_get_info
from project import settings
from orders.views import *
from orders.api import api_get_orders
from orders.views import cart
from orders import views
from orders.api import api_get_more
from orders.api import edit_product
from django.conf import settings
from orders.views import sda
from orders.api import add_order
from orders.api import order_status

urlpatterns = [
    path('logout/',
         LogoutView.as_view(
             template_name='',
             next_page=None
         ),
         name='logout'
         ),
    path('admin/', admin.site.urls),
    path('',main_page,name="main_page"),
    path('main', main_page,name=""),
    path('getitems',api_get_info),
    path("del/<int:id>", dell_items, name="dell"),
    path("cart", cart),
    path("cartitems",api_get_orders),

    path('cart/add/<int:id>/', views.cart_add),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    path("api/get-more/<int:id>",api_get_more),
    path("edit/product", edit_product, name="edit_product"),
    path("add_order", add_order, name='CartAdd'),
    path("orders", sda, name="orders"),
    path("orders/changestatus/<int:id>", order_status, name="orders_status"),
    path('login/',LoginView.as_view(template_name='account/login.html'),name='login')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



