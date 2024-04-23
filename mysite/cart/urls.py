from django.urls import path
from cart.views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_summary, name="cart_summary"),
    path('cart/', view_cart ),

]
