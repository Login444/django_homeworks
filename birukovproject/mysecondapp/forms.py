from django import forms


class GameForm(forms.Form):
    game = forms.ChoiceField(label='Choose the game' ,choices=[('Coin', 'Монета'), ('Cube','Кубик'), ('Number','Число')],
                             widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    count = forms.IntegerField(label='Count of tries', min_value=1, max_value=64,
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Введите число попыток от 1 до 64'}))