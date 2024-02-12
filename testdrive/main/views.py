from django.shortcuts import render
from .models import Cars


def index(request):
    cars = Cars.objects.order_by('id')
    print(cars)
    return render(request, 'main/index.html', {'title': 'Главная страница',
                                               'cars': cars})
