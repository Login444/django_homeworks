from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_product_form, name='update_product_form'),
    path('orders/<int:client_id>/<int:time_diapazone>', views.products_list, name='product_list'),
    path('upload/', views.upload_img_for_product, name='upload_img_for_product'),
]
