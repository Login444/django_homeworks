import decimal

from django.core.management.base import BaseCommand
from random import randint
from marketapp.models import Order, Client, Product

class Command(BaseCommand):
    help = "Create 10 random orders"

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            client = Client.objects.get(id=i)
            order = Order(client=client,
                          total_price=decimal.Decimal(randint(100, 1000)))
            order.save()
            for j in range(1, 11):
                product = Product.objects.get(id=j)
                order.products.add(product)
            self.stdout.write(f'{order}')