from django.contrib import admin

# Register your models here.
from myapp.form import CustomerForm
from myapp.models import *

admin.site.register(Product)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'get_jalai_date_birthday', 'mobile', 'email')
    form = CustomerForm


admin.site.register(Customer, CustomerAdmin)


class OrderAppAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'price', 'num', 'price_all', 'create_at', 'update_at')
    raw_id_fields = ['product']


admin.site.register(OrderApp, OrderAppAdmin)

