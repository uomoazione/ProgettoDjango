from django.shortcuts import render
from .models import *


# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer= request.user.customer
        order, created= Order.objects.get_or_create(customer=customer, complete=False) #creiamo un oggetto o lo mettiamo in query se esiste già
        items=order.orderitem_set.all()
    else:
        items=[]
    context = {'items': items} # Aggiungi gli oggetti items al contesto
    return render(request, "store/cart.html", context)

def checkout(request):
    context = {}
    return render(request, "store/checkout.html", context)
