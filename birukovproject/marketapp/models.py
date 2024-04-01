from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    adress = models.TextField(max_length=500)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Client_name: {self.name}; '
                f'email: {self.email}; '
                f'phone: {self.phone}; '
                f'adress: {self.adress}; '
                f'registration_date: {self.registration_date}')


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=1500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)


class Order(models.Model):
    products = models.ManyToManyField(Product)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)
