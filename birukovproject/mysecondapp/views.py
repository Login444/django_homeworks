import logging
from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
from .models import CoinThrows, Author
from datetime import date
from .forms import GameForm


# Create your views here.
logger = logging.getLogger(__name__)

def game_form(request):
    if request.method == 'POST':
        form = GameForm(request.POST).as_table()
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'Coin':
                return coin(request, count)
            elif game == 'Cube':
                return cube(request, count)
            else:
                return random_num(request, count)
    else:
        form = GameForm()
        return render(request,
                      'mysecondapp/game_choice.html',
                      {'form': form, 'title': 'Choose the game'})


def coin(request, count):
    result_list = []
    for _ in range(1, count+1):
        result = choice(['Орёл', 'Решка'])
        throw = (_, result)
        result_list.append(throw)
        # throw_res = models.CoinThrows(throw_result=result)
        # throw_res.save()
        logger.info(f'После броска моентки выпало: {result}')
    return render(request,
                  'mysecondapp/game_results.html',
                  {'result_list': result_list, 'title': 'Results'})

def coin_stat(request):
    data = models.CoinThrows.stat_coin(request)
    return HttpResponse(f'{data}')

def cube(request, count):
    result_list = []
    for _ in range(1, count+1):
        result = randint(1, 6)
        throw = (_, result)
        result_list.append(throw)
        logger.info(f'После броска кубика выпало: {result}')
    return render(request,
                  'mysecondapp/game_results.html',
                  {'result_list': result_list, 'title': 'Results'})

def random_num(request, count):
    result_list = []
    for _ in range(1, count+1):
        result = randint(0, 100)
        throw = (_, result)
        result_list.append(throw)
        logger.info(f'Случайное число: {result}')
    return render(request,
                  'mysecondapp/game_results.html',
                  {'result_list': result_list, 'title': 'Results'})

# def create_authors(request):
#     result = []
#     for i in range(10):
#         author = Author(name=f'Name{i}', lastname=f'Lastname{i}', email=f'example{i}@mail.ru', biography=f'Biography{i}', birthday=date.today())
#         author.save()
#         result.append(author.fullname())
#     return HttpResponse(f'{result}')