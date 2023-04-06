from django.shortcuts import render
from .models import *


# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)  # creiamo un oggetto o lo mettiamo in query se esiste già
        items = order.orderitem_set.all()
    else:
        items = []
        order= {'get_cart_total':0, 'get_cart_items':0}
    context = {'items': items, 'order': order}  # Aggiungi gli oggetti items al contesto
    return render(request, "store/cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)  # creiamo un oggetto o lo mettiamo in query se esiste già
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, "store/checkout.html", context)
