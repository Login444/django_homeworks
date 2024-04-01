import decimal

from django.core.management.base import BaseCommand
from random import randint
from marketapp.models import Product

class Command(BaseCommand):
    help = "Create 10 random products"

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(name=f'Product{i}',
                              description=f'Description{i}',
                              price=decimal.Decimal(randint(1, 10)),
                              count=randint(10,50))
            product.save()
            self.stdout.write(f'{product}')