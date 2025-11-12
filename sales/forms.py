from django import forms
from .models import Customer, Order, OrderItem

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("full_name", "email", "is_active")

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("customer", "notes")

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ("product", "quantity", "unit_price")
