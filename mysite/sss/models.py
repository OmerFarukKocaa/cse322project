from django.db import models


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    postcode = models.SmallIntegerField()

    def __str__(self):
        return " ".join([self.street, self.city, self.state, str(self.postcode)])


class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BillingAddress(Address):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shippingaddress = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.customer) + " @ " + str(self.shippingaddress)


class OrderPayment(models.Model):
    cardNumber = models.BigIntegerField()
    txnId = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    billingaddress = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
