from datetime import date
from django.shortcuts import render
from bmstu_lab.models import Mins

from django.views.generic import TemplateView

orders = [{'title': 'Аметист', 'id': 1, 'from': 'Мадагаскар',
           'img': 'https://static.mineralmarket.ru/img/p/439373-1727477.jpg',
           'definition': 'Аметист - фиолетовая разновидность кварца. Прозрачный аметист относится к полудрагоценным камням.'},
          {'title': 'Флюорит', 'id': 2, 'from': 'Монголия',
           'img': 'https://cs1.livemaster.ru/storage/8d/e8/5bcd02e92a9d6a06acdc414374sf--fen-shuj-i-ezoterika-flyuorit-srez.jpg',
           'definition': 'Флюорит - плавиковый шпат. Хрупок, окрашен в различные цвета от розового, жёлтого и оранжевого до синего, зеленого и фиолетового.'},
          {'title': 'Кварц', 'id': 3, 'from': 'Урал', 'img': 'https://static.mineralmarket.ru/img/p/282546-1128195.jpg',
           'definition': 'Кварц (горный хрусталь) - природный диоксид кремния, самый распространённый минерал на земле. Чистые кристаллы встречаются редко и высоко ценятся коллекционерами.'}
          ]


#def GetOrders(request):
 #   return render(request, 'orders.html', {'data': {
  #      'current_date': date.today(),
   #     'orders': orders
    #}})


def mineralList(request):
    return render(request, 'orders.html', {'data': {
        'current_date': date.today(),
        'mins': Mins.objects.all()
    }})


def GetOrder(request, id):
    return render(request, 'order.html', {'data': {
        'current_date': date.today(),
        'mineral': Mins.objects.filter(id_min=id)[0],
        #'id': id,
        'img': orders[id - 1]['img'],
        #'definition': orders[id - 1]['definition']
    }})
