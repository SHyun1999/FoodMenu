from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    return HttpResponse("<h1>annyeong!</h1>")


def item(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)