from django.shortcuts import render
from .models import Product

def homepage(request):
    guns = Product.objects.order_by("-price")
    return render(request, 'website/product_list.html', {"weapons": guns})

def knifes(request):
    knifes = Product.objects.filter(category="Knife")
    return render(request, 'website/product_list.html', {"weapons": knifes})

def pistols(request):
    pistols = Product.objects.filter(category="Pistol")
    return render(request, 'website/product_list.html', {"weapons": pistols})

def awps(request):
    awps = Product.objects.filter(category="AWP")
    return render(request, 'website/product_list.html', {"weapons": awps})

def riflers(request):
    riflers = Product.objects.filter(category="Rifler")
    return render(request, 'website/product_list.html', {"weapons": riflers})

def gloves(request):
    gloves = Product.objects.filter(category="Glove")
    return render(request, 'website/product_list.html', {"weapons": gloves})