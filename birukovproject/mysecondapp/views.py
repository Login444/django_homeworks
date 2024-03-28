import logging
from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint

# Create your views here.
logger = logging.getLogger(__name__)
def coin(request):
    result = choice(['Орёл', 'Решка'])
    logger.info(f'После броска моентки выпало: {result}')
    return HttpResponse(f'<h1>После броска моентки выпало: {result}</h1>')

def cube(request):
    result = randint(1, 6)
    logger.info(f'После броска кубика выпало: {result}')
    return HttpResponse(f'<h1>После броска кубика выпало: {result}</h1>')

def random_num(request):
    result = randint(0, 100)
    logger.info(f'Случайное число: {result}')
    return HttpResponse(f'<h1>Случайное число: {result}</h1>')