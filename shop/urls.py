from django.urls import path

from .views import *

urlpatterns = [
    path('product', productView, name='product'),
    path('product/<slug:slugInput>', detailView, name='detail'),
    path('cart', cartView, name='cart'),
    path('', index, name='index')
]
