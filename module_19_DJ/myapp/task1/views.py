from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *

def func(request):
    sp = ['Главная', 'Магазин', 'Корзина']
    context = {
        'sp': sp,
    }
    return render(request, 'platform.html', context)

def games(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')

def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {
        'error': '',
        'Byuer': users,
    }
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        r_pass = request.POST.get('r_pass')
        age = request.POST.get('age')
        sp = []
        for i in users:
            sp.append(i.name)
        if login in sp:
            fail = 'Пользователь уже существует'
            info = {
                'error': fail,
            }
        elif password != r_pass:
            fail = 'Пароли не совпадают'
            info = {
                'error': fail,
            }
        elif int(age) < 18:
            fail = 'Вы должны быть старше 18'
            info = {
                'error': fail,
            }
        else:
            Buyer.objects.create(name=login, balance=2000, age=age)
            return render(request, 'platform.html')

    return render(request, 'registration_page.html', context=info)

# def sign_up_by_django(request):
#     users = Buyer.objects.all()
#     info = {
#         'error': '',
#         'Buyer': users,
#     }
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         users = Buyer.objects.all()
#         info = {
#             'error': '',
#             'Buyer': users,
#         }
#         if form.is_valid():
#             login = form.cleaned_data['login']
#             password = form.cleaned_data['password']
#             r_pass = form.cleaned_data['r_pass']
#             age = form.cleaned_data['age']
#             sp = []
#             for i in users:
#                 sp.append(i.name)
#             if login in sp:
#                 fail = 'Пользователь уже существует'
#                 info = {
#                     'error': fail,
#                 }
#                 return render(request, 'registration_page.html', context=info)
#             elif password != r_pass:
#                 fail = 'Пароли не совпадают'
#                 info = {
#                     'error': fail,
#                 }
#                 return render(request, 'registration_page.html', context=info)
#             elif int(age) < 18:
#                 fail = 'Вы должны быть старше 18'
#                 info = {
#                     'error': fail,
#                 }
#                 return render(request, 'registration_page.html', context=info)
#             Buyer.objects.create(name=login, balance=2000, age=age)
#
#     else:
#         form = UserRegister()
#     return render(request, 'registration_page.html', {'form': form})
#
#

