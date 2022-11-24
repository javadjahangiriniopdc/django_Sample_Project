from django.contrib import admin

# Register your models here.
from myapp.form import CustomerForm
from myapp.models import *

admin.site.register(City)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'get_jalali_date_birthday', 'mobile', 'email', 'get_city')
    form = CustomerForm


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_tag')


admin.site.register(Product, ProductAdmin)


class OrderAppAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'price', 'num', 'price_all', 'create_at', 'update_at')


admin.site.register(OrderApp, OrderAppAdmin)
