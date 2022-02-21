from django.shortcuts import render
from django.views.generic import ListView
from .models import Skin, Category

class MainTemplateView(ListView):
    template_name = 'website/product_list.html'
    context_object_name = 'weapons'
    queryset = Skin.objects.all()

class KnifesView(MainTemplateView):
    queryset = Skin.objects.filter(category__name__contains="Knife")

class PistolsView(MainTemplateView):
    queryset = Skin.objects.filter(category__name__contains="Pistol")

class AWPsView(MainTemplateView):
    queryset = Skin.objects.filter(category__name__contains="AWP")

class RiflersView(MainTemplateView):
    queryset = Skin.objects.filter(category__name__contains="Rifler")

class GlovesView(MainTemplateView):
    queryset = Skin.objects.filter(category__name__contains="Glove")
