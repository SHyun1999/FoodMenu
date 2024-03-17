from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

def index(request):
    return HttpResponse("<h1>annyeong!</h1>")


def item(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }

    return render(request, 'food/index.html', context)