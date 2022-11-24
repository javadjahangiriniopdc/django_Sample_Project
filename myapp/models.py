from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from jalali_date import date2jalali
from django.utils.html import format_html


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام شهر')

    def __str__(self):
        return self.name


class Customer(models.Model):
    username = models.CharField(max_length=20, verbose_name='نام کاربری')
    first_name = models.CharField(max_length=25, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    birthday = models.DateTimeField(null=True, verbose_name='تاریخ تولد')
    mobile = models.CharField(max_length=20, verbose_name='موبایل')
    email = models.EmailField(verbose_name='ایمیل')
    city = models.ManyToManyField(City, verbose_name='شهر')

    def __str__(self):
        return self.first_name + '-' + self.last_name

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    def get_jalali_date_birthday(self):
        return date2jalali(self.birthday)

    get_jalali_date_birthday.short_description = 'تاریخ تولد'

    def get_city(self):
        cites = Customer.objects.get(id=self.id).city.all()
        out = ''
        for city in cites:
            if city.name:
                out += f'<li>{city.name}</li> '
        return format_html(out)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    price = models.IntegerField(verbose_name='قیمت')
    img = models.ImageField(upload_to='product_img', null=True, blank=True, verbose_name='عکس')

    def image_tag(self):
        return mark_safe('<img src="%s" width="50"  />' % self.img.url)

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

    def get_jalali_date_creat_at(self):
        return date2jalali(self.create_at)

    def get_jalali_date_update_at(self):
        return date2jalali(self.update_at)

    def get_time_create_at(self):
        return self.create_at.strftime('%H:%M:%S')
