from django.urls import path
from app import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('product-detail/<int:id>',Product_detailView.as_view(), name='product-detail'),
    path('cart/<int:id>', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart,name='show-cart'),
    path('pluscart/',views.pluscart,name='pluscart'),
    path('minuscart/',views.minuscart,name='minuscart'),
    path('removecart/',views.removecart,name='removecart'),
    path('orderplaced/', views.order_placed, name='order_placed'),
   
    path('profile/', ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>',mobile, name='mobiledata'),
    
    path('laptop/',laptop, name='laptop'),
    path('laptop/<slug:data>',laptop, name='laptopdata'),
    path('women/',women, name='women'),
    path('women/<slug:data>',women, name='womendata'),
    path('men/',men, name='men'),
    path('men/<slug:data>',men, name='mendata'),
  
    path('checkout/', views.checkout, name='checkout'),
    path('order_address/', views.orderaddress, name='orderaddress'),
    path('search/', views.search, name='search'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
