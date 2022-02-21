from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class MainTemplateView(ListView):
    template_name = 'website/product_list.html'
    context_object_name = 'weapons'
    queryset = Product.objects.all()

class KnifesView(MainTemplateView):
    queryset = Product.objects.filter(category="Knife")

class PistolsView(MainTemplateView):
    queryset = Product.objects.filter(category="Pistols")

class AWPsView(MainTemplateView):
    queryset = Product.objects.filter(category="AWP")

class RiflersView(MainTemplateView):
    queryset = Product.objects.filter(category="Rifler")

class GlovesView(MainTemplateView):
    queryset = Product.objects.filter(category="Glove")
