from django.core.management.base import BaseCommand
from marketapp.models import Client
from random import randint

class Command(BaseCommand):
    help = "Create 10 random clients"

    def handle(self, *args, **kwargs):
        for i in range(10):
            client = Client(name=f'Client{i}',
                            email=f'mail{i}@example.com',
                            phone=randint(89000000000, 89999999999),
                            adress=f'Adress{i}')
            client.save()
            self.stdout.write(f'{client}')