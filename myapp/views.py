from django.shortcuts import render

# Create your views here.
from .models import *
import time
from django.db import connection, reset_queries


def debgger(func):
    def wrapper(*args, **kwargs):
        reset_queries()
        st = time.time()
        value = func(*args, **kwargs)
        et = time.time()
        queries = len(connection.queries)
        print(connection.queries)
        print(f"connection number:{queries} \n taketime={et - st}:.3f")
        return value

    return wrapper


@debgger
def home(request):
    # orderapps = OrderApp.objects.select_related('customer', 'product').filter(customer__first_name='جواد',product__name='گل')
    # orderapps = OrderApp.objects.filter(customer__first_name='جواد', product__name='گل')

    # orderapps = OrderApp.objects.filter(customer__first_name='جواد')
    # orderapps = OrderApp.objects.select_related('customer').filter(customer__first_name='جواد')
    context = {'orderapps': orderapps}
    return render(request, 'myapp/index.html', context)
