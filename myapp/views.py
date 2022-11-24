from django.shortcuts import render

# Create your views here.
from .models import *


def home(request):
    # orderapps = OrderApp.objects.filter(customer__first_name='جواد' , product__name='گل')
    orderapps = OrderApp.objects.filter(customer__first_name='جواد' )
    context = {'orderapps': orderapps}
    return render(request, 'myapp/index.html', context)
