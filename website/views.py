from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product

class HomepageView(TemplateView):
    template_name = 'website/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weapons'] = Product.objects.order_by("-price")
        return context

class KnifesView(TemplateView):
    template_name = 'website/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weapons'] = Product.objects.filter(category="Knife")
        return context

class PistolsView(TemplateView):
    template_name = 'website/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weapons'] = Product.objects.filter(category="Pistols")
        return context

class AWPsView(TemplateView):
    template_name = 'website/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weapons'] = Product.objects.filter(category="AWP")
        return context

class RiflersView(TemplateView):
    template_name = 'website/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weapons'] = Product.objects.filter(category="Rifler")
        return context

class GlovesView(TemplateView):
    template_name = 'website/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weapons'] = Product.objects.filter(category="Glove")
        return context
