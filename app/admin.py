from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.

from typing import List
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    model=Customer
    list_display=['Id','User','Name','Locality','City','State','ZipCode']
    


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['Id','Title','Selling_price','Discounted_Price','Descriptio','Brand','Category','Product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    model=Cart
    list_display=['Id','User','Product','Quantity']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    model=Order
    list_display=['Id','User','Product','product_info','Customer','customer_info','Quantity','Status']

    def customer_info(self,obj):
        link=reverse("admin:app_customer_change",args=[obj.Customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.Customer.Name)

    def product_info(self,obj):
        link=reverse("admin:app_product_change",args=[obj.Product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.Product.Title)


