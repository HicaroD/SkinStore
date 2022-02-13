from django.shortcuts import render
from .models import Product

def homepage(request):
    return render(request, 'website/base.html')

def knifes(request):
    knifes = Product.objects.filter(category="Knife")
    return render(request, 'website/knife.html', {"knifes": knifes})
