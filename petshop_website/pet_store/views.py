from django.shortcuts import render
from .models import Product
# Create your views here.


def home(request):
    products = Product.objects.all()

    return render(request, 'pet_store/home.html', {'products': products})

def store(request):
    products = Product.objects.all()

    return render(request, 'pet_store/store.html', {'products': products})

def test(request):
    products = Product.objects.all()

    return render(request, 'pet_store/test.html', {'products': products})