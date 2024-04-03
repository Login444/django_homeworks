from django.shortcuts import render, HttpResponse
from .models import Client, Product, Order
from datetime import datetime, timedelta


# Create your views here.

def products_list(request, client_id: int, time_diapazone: int):
    client = Client.objects.get(pk=client_id)
    start_date = datetime.now() - timedelta(days=time_diapazone)
    orders = Order.objects.filter(client=client, order_date__gte=start_date).prefetch_related('products').order_by(
        '-order_date')
    products = set()
    for order in orders:
        products |= set(order.products.all())
    return render(request,
                  'marketapp/orders_by_client.html',
                  {'title': "Orders", 'products': products, 'client_name': client.name, 'time': time_diapazone})
