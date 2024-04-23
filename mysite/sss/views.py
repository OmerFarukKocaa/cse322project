from django.shortcuts import render, redirect
from django.contrib import messages
from sss.forms import CustomerForm, ProductForm
from sss.models import Customer, Product
from django.http import HttpResponse


def create_customer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            c = Customer(name=name)
            # data saved to the DB
            c.save()
            messages.success(request, f'{c.name} saved!')

            # redirect to a confirmation page if successful
            return render(request, "model_saved.html", {"messages": messages.get_messages(request), 'redirect': '/sss'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()

    return render(request, 'sss_create_customer.html', {'form': form, 'redirect': '/sss/create'})


def home(request):
    products = Product.objects.all()
    return render(request, "sss_home.html", {'products': products})


def get_customer(request):
    if request.GET:
        name_filter = request.GET.get('name_filter', '')
        customers = Customer.objects.filter(name=name_filter)
        return render(request, "sss_search_customer.html", {"customers": customers})

    else:
        return render(request, "sss_search_customer.html")


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            product = Product(name=name, price=price, image=image)
            product.save()
            messages.success(request, f'{product.name} saved!')
            return render(request, "model_saved.html", {"messages": messages.get_messages(request), 'redirect': '/sss'})
        else:
            messages.error(request, "Form is not valid!")
    else:
        form = ProductForm()

    return render(request, 'sss_product.html', {'form': form, 'redirect': '/sss/'})
