from django.contrib import admin
from sss.models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(BillingAddress)
admin.site.register(Order)
admin.site.register(OrderPayment)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(CartItem)