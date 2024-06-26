from django.core.management.base import BaseCommand
from marketapp.models import Product


class Command(BaseCommand):
    help = "Delete Product by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'{product}\nDELETED')
