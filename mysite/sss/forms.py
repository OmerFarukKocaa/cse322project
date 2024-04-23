import django.forms.widgets
from django.forms import ModelForm, Textarea, TextInput, ChoiceField, FileInput
from sss.models import Customer, Product


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


# class ProductUpdateForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ["name", "price", "image"]
#         widgets = {
#             "name": TextInput(attrs={"size": 40}),
#             "image": FileInput(),
#         }
