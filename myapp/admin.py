from django.contrib import admin

# Register your models here.
from myapp.models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderApp)
