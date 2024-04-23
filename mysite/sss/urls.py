from django.urls import path
from sss.views import home, get_customer, create_customer, add_product

urlpatterns = [
    path('', home),
    path('search/', get_customer),
    path('create/', create_customer, name='create_customer'),
    path('add_product/', add_product, name='add_product'),
]
