from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
# from task1.forms import ContactForm
# from rest_framework import generics
from .models import *


# from .serializers import *


# class GameAPIView(generics.ListAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer


# def main_page(requests):
#     return render(requests, 'main.html', context={'title': 'Главная страница'})


# def games(request):
#     posts = Game.objects.all().order_by('-size')
#     paginator = Paginator(posts, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'pagination.html', {'page_obj': page_obj, 'title': 'Игры'})

def games(requests):
    title = 'Игры'
    games = Game.objects.all()
    # dates = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', 'Doom']
    # releases = [f'{date}' for i, date in enumerate(dates, start=1)]
    # dates = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2", "Doom"]}
    # releases = [f'{date}' for date in games]
    context = {'title': title,
               'releases': games}
    return render(requests, 'games.html', context=context)


# def cart(requests):
#     title = 'Корзина'
#     cart_ = 'Ваша корзина пуста'
#     context = {'title': title,
#                'cart': cart_}
#     return render(requests, 'cart.html', context=context)

def cart(requests):
    title = 'Корзина'
    carts = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2", "Doom"]}
    releases = [f'{i}' for i in carts['games']]
    context = {'title': title,
               'carts': releases}
    return render(requests, 'cart.html', context=context)


# def games2(request):
#     games_ = Game.objects.all().order_by('-size')
#     items_per_page = request.GET.get('items_per_page', 5)
#     paginator = Paginator(games_, items_per_page)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {'page_obj': page_obj, 'items_per_page': items_per_page}
#     return render(request, 'pagination2.html', context=context)

"""
<QueryDict: {
    'csrfmiddlewaretoken': ['nT7OLODH71IDWxzKqPj4QqwXhRS170GoUbZSn9oLMz59yeg07SdRtIKYlX34LaBZ'],
    'username': ['admin2'],
    'password': ['adminadmin'],
    'repeat_password': ['adminadmin'],
    'age': ['52']}>
"""


def sign_up(request):
    buyers = Buyer.objects.all()
    info = {}
    error = ''

    if request.method == 'POST':
        print(160 * '-')
        username = request.POST.get('username')
        age = request.POST.get('age')
        # for key in ('username', 'balance', 'age'):
        # for key in ('username', 'age'):
        #     info[key] = request.POST.get(key, '')

        if username not in [buyer.name for buyer in buyers]:
            Buyer.objects.create(name=username,
                                 age=age,
                                 balance=1000)
            # return render(request, 'registration_page.html',
            #               context={'wellcome': f'Приветствуем, {username}!'})
        else:
            username, user_name = None, username
            error = f'Пользователь {user_name} уже зарегистрирован!'


    context = {'title': 'Регистрация', 'error': error, 'username': username}
    return render(request, 'registration_page.html', context=context)
