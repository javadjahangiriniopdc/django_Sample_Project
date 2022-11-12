from django.db import models


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20, verbose_name='نام کاربری')
    first_name = models.CharField(max_length=25, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    mobile = models.CharField(max_length=20, verbose_name='موبایل')
    email = models.EmailField(verbose_name='ایمیل')

    def __str__(self):
        return self.first_name + '-' + self.last_name

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    price = models.IntegerField(verbose_name='قیمت')
    img = models.ImageField(upload_to='product_img', null=True, blank=True, verbose_name='عکس')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name


class OrderApp(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='مشتری')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='محصولات')
    price = models.IntegerField(verbose_name='قیمت')
    num = models.IntegerField(verbose_name='تعداد')
    price_all = models.IntegerField(verbose_name='قیمت کل')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    update_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    def __str__(self):
        return self.customer.first_name + '-' + self.customer.last_name + '-' + self.product.name

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'