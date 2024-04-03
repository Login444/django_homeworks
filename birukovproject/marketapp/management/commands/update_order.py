from django.core.management.base import BaseCommand
from marketapp.models import Order


class Command(BaseCommand):
    help = "Update order by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('product', type=int, help="Product ID")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product_id = kwargs.get('product')
        order = Order.objects.filter(pk=pk).first()
        order.products.clear()
        order.products.add(product_id)
        order.save()
        self.stdout.write(f'{order}')