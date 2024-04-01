import logging
from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
from .models import CoinThrows, Author
from datetime import date


# Create your views here.
logger = logging.getLogger(__name__)
def coin(request):
    result = choice(['Орёл', 'Решка'])
    throw_res = models.CoinThrows(throw_result=result)
    throw_res.save()
    logger.info(f'После броска моентки выпало: {result}')
    return HttpResponse(f'<h1>После броска моентки выпало: {result}</h1>')

def coin_stat(request):
    data = models.CoinThrows.stat_coin(request)
    return HttpResponse(f'{data}')

def cube(request):
    result = randint(1, 6)
    logger.info(f'После броска кубика выпало: {result}')
    return HttpResponse(f'<h1>После броска кубика выпало: {result}</h1>')

def random_num(request):
    result = randint(0, 100)
    logger.info(f'Случайное число: {result}')
    return HttpResponse(f'<h1>Случайное число: {result}</h1>')

def create_authors(request):
    result = []
    for i in range(10):
        author = Author(name=f'Name{i}', lastname=f'Lastname{i}', email=f'example{i}@mail.ru', biography=f'Biography{i}', birthday=date.today())
        author.save()
        result.append(author.fullname())
    return HttpResponse(f'{result}')