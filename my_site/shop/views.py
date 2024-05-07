from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    products = models.Shop.objects.all()
    return render(request, 'shop/index.html', {'products': products, 'title': 'Список товаров'})
