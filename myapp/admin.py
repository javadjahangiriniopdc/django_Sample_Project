from django.contrib import admin

# Register your models here.
from myapp.form import CustomerForm
from myapp.models import *


admin.site.register(Product)
admin.site.register(OrderApp)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'get_jalai_date_birthday', 'mobile', 'email')
    form = CustomerForm


admin.site.register(Customer, CustomerAdmin)
