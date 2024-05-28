from django.shortcuts import render
from sss.models import Product, CartItem, Customer


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request, 'sss_home.html', {'products': products})


def view_cart(request):
    cart_items = CartItem.objects.filter(customer=request.customer)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart_item, created = CartItem.objects.get_or_create(product=product,
#                                                         customer=request.customer)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect('cart:view_cart')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    customer = Customer.objects.first()  # Replace with logic to get the current logged-in customer
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart_item, created = CartItem.objects.get_or_create(
                product=product,
                customer=customer,
                defaults={'quantity': form.cleaned_data['quantity']}
            )
            if not created:
                cart_item.quantity += form.cleaned_data['quantity']
                cart_item.save()
            messages.success(request, f'{product.name} added to cart!')
            return redirect('cart:view_cart')
    else:
        form = CartItemForm(initial={'product': product, 'quantity': 1})

    return render(request, 'add_to_cart.html', {'form': form, 'product': product})


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')


# def cart_summary(request):
#     return render(request, "cart.html", {})

# def cart_summary(request):
#     customer = Customer.objects.first()  # Replace with logic to get the current logged-in customer
#     cart_items = CartItem.objects.filter(customer=customer)
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def cart_summary(request):
    cart_items = [
        {'quantity': 2, 'product': {'name': 'Product A', 'price': 10.00}},
        {'quantity': 1, 'product': {'name': 'Product B', 'price': 20.00}},
    ]

    for item in cart_items:
        item['total_price'] = item['quantity'] * item['product']['price']

    totals = sum(item['total_price'] for item in cart_items)

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'totals': totals})