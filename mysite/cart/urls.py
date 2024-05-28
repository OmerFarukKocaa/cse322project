from django.urls import path
from cart.views import *

app_name = 'cart'

# urlpatterns = [
#     path('', cart_summary, name="cart_summary"),
#     path('cart/', view_cart ),
#     # path('view/', view_cart, name='view_cart'),
#     # path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
#     # path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
#
# ]

urlpatterns = [
    path('', product_list, name='product_list'),
    # path('cart/', cart\views.home, name='home'),
    path('cart/', view_cart, name='view_cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]