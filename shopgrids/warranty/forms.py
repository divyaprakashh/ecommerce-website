# warranty/forms.py
from django import forms
from .models import Warranty
from cart.models import Order

from productmanagement.models import Products  # Import Products model

class WarrantyForm(forms.ModelForm):
    order = forms.ModelChoiceField(queryset=Order.objects.all(), label="Order ID")
    product = forms.ModelChoiceField(queryset=Products.objects.all(), label="Product")  # Add product field

    class Meta:
        model = Warranty
        fields = ['order', 'product', 'start_date', 'end_date']
