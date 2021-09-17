from django.shortcuts import render
from .models import Product, SpecProduct


def index(request):
    context = {
        'title': 'OX | Home'
    }

    return render(request, 'index.html', context)


def productView(request):
    model_product = Product.objects.all()
    context = {
        'title': 'OX | Products',
        'products': model_product
    }

    return render(request, 'shop/store.html', context)


def detailView(request, slugInput):
    items = Product.objects.get(slug=slugInput)
    spec = SpecProduct.objects.all().values()
    context = {
        'title': f'OX | {items.name}',
        'items': items,
        'spec': spec
    }

    return render(request, 'shop/detail.html', context)


def cartView(request):
    context = {
        'title': 'OX | Cart'
    }

    return render(request, 'shop/cart.html', context)
