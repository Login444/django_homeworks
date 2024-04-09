from django import forms
from .models import Product

class UpdateProduct(forms.Form):
    @staticmethod
    def choices_list():
        products = Product.objects.all()
        list_of_choices = []
        for product in products:
            res_tuple = (product.pk, product.name)
            list_of_choices.append(res_tuple)
        return list_of_choices

    name = forms.ChoiceField(label='Выберите товар: ', choices=choices_list(),
                             widget=forms.Select(attrs={'class': 'form-check-input'}))
    new_name = forms.CharField(label='Введите новое название товара (если необходимо)',
                               min_length=3, max_length=120,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Новое название'}))
    description = forms.CharField(min_length=3, max_length=1500,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Введите описание товара'}))
    price = forms.DecimalField(label='Укажите стоимость товара', min_value=1,
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Стоимость'}))
    count = forms.IntegerField(label='Укажите колличество товара на складе', min_value=0,
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Остаток на складе'}))


class UploadProductImage(forms.Form):
    @staticmethod
    def choices_list():
        products = Product.objects.all()
        list_of_choices = []
        for product in products:
            res_tuple = (product.pk, product.name)
            list_of_choices.append(res_tuple)
        return list_of_choices

    name = forms.ChoiceField(label='Выберите товар: ', choices=choices_list(),
                             widget=forms.Select(attrs={'class': 'form-check-input'}))
    image = forms.ImageField(label='Загрузите изображение')