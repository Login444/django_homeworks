from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponse
from .models import Client, Product, Order
from datetime import datetime, timedelta
from .forms import UpdateProduct, UploadProductImage


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

def update_product_form(request):
    if request.method == 'POST':
        form = UpdateProduct(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_name = form.cleaned_data['new_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            product = Product.objects.filter(pk=name).first()
            if new_name != '':
                product.name = new_name
            product.description = description
            product.price = price
            product.count = count
            product.save()
            return HttpResponse(f'<p>{product} - Изменения добавлены</p>')
    else:
        form = UpdateProduct()
        return render(request, 'marketapp/update_product.html', {'form': form, 'title': 'Updating product'})

def upload_img_for_product(request):
    if request.method == 'POST':
        form = UploadProductImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            pk = form.cleaned_data['name']
            file = FileSystemStorage()
            file.save(image.name, image)
            product = Product.objects.filter(pk=pk).first()

    else:
        form = UploadProductImage()
        return render(request, 'marketapp/update_product.html', context={'form': form, 'title': 'Uploading image'})