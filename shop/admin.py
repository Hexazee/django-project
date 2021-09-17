from shop.models import ShippingAddress
from django.contrib import admin
from .models import *
LIST_MODELS = [Customer, Product, Order, OrderItem, ShippingAddress, SpecProduct]

for item in LIST_MODELS:
    admin.site.register(item)
