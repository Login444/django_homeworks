from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_form, name='game_form'),
    path('coin/<int:count>', views.coin, name='coin'),
    path('cube/<int:count>', views.cube, name='cube'),
    path('random_num/<int:count>', views.random_num, name='random_num'),
    path('coin_stat/', views.coin_stat, name='stat_coin'),
    # path('authors/', views.create_authors, name='authors')
]