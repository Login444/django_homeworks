from django.core.management.base import BaseCommand
from marketapp.models import Product


class Command(BaseCommand):
    help = "Update product by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product ID')
        parser.add_argument('name', type=str, help='product name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.save()
        self.stdout.write(f'{product}')
