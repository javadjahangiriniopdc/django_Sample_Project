from django.forms import ModelForm, Textarea
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

from myapp.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 1}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['birthday'] = JalaliDateField(label=('تاریخ تولد'),  # date format is  "yyyy-mm-dd"
                                                  widget=AdminJalaliDateWidget  # optional, to use default datepicker
                                                  )


