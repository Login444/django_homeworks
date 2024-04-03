from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:client_id>/<int:time_diapazone>', views.products_list, name='product_list'),
]
