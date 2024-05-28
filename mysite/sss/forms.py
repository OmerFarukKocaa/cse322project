import django.forms.widgets
from django.forms import ModelForm, Textarea, TextInput, ChoiceField, FileInput, NumberInput
from sss.models import Customer, Product, CartItem, Order, Address, BillingAddress, OrderNew


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={"size": 20}),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "image"]
        widgets = {
            "name": TextInput(attrs={"size": 40}),
            "image": FileInput(),
        }


class CartItemForm(ModelForm):
    class Meta:
        model: CartItem
        fields = ["product", "quantity"]
        widgets = {
            "quantity": NumberInput(attrs={'min': 1, 'value': 1}),
        }


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "image"]
        widgets = {
            "name": TextInput(attrs={"size": 40}),
            "image": FileInput(),
        }


class OrderForm(ModelForm):
    class Meta:
        model = OrderNew
        fields = ["customer_name", "product_name", "quantity", "shipping_address", "billing_address"]
        widgets = {
            "customer_name": TextInput(attrs={"size": 40}),
            "product_name": TextInput(attrs={"size": 40}),
            "quantity": NumberInput(attrs={'min': 1, 'value': 1}),
            "shipping_address": TextInput(attrs={"size": 40}),
            "billing_address": TextInput(attrs={"size": 40}),
        }