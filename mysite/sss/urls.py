from django.urls import path
from sss.views import home, get_customer, create_customer, add_product, create_order, get_order, get_product

urlpatterns = [
    path('', home),
    path('search/', get_customer),
    path('create/', create_customer, name='create_customer'),
    path('add_product/', add_product, name='add_product'),
    path('create_order/', create_order, name='create_order'),
    path('search_order/', get_order, name='search_order'),
    path('search_product/', get_product, name='search_product'),

]
