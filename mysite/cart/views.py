from django.shortcuts import render
from sss.models import Product, CartItem


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request, 'sss_home.html', {'products': products})


def view_cart(request):
    cart_items = CartItem.objects.filter(customer=request.customer)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                        customer=request.customer)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')


def cart_summary(request):
    return render(request, "cart.html", {})
