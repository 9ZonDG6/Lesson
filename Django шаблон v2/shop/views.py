from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    products = models.Shop.objects.all()
    categories = models.Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'title': 'Список товаров',
    }
    return render(request, 'shop/index.html', context=context)


def get_category(request, category_id):
    products = models.Shop.objects.filter(category=category_id)
    categories = models.Category.objects.all()
    # category = models.Category.objects.get(pk=category_id)
    category = get_object_or_404(models.Category, pk=category_id)
    context = {
        'products': products,
        'categories': categories,
        'category': category,
    }
    return render(request, 'shop/category.html', context=context)
