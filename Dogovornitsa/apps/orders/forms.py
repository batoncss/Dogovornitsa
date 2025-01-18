from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = ['name', 'body', 'template', 'participant_1', 'participant_2']

