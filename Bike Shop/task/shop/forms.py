from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'your name'
        self.fields['surname'].label = 'your surname'
        self.fields['phone_number'].label = 'your phone number'

    class Meta:
        model = Order
        fields = ('name', 'surname', 'phone_number')
