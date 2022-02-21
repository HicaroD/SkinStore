from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainTemplateView.as_view(), name="homepage"),
    path('knifes/', views.KnifesView.as_view(), name="knifes"),
    path('gloves/', views.GlovesView.as_view(), name="gloves"),
    path('pistols/', views.PistolsView.as_view(), name="pistols"),
    path('riflers/', views.RiflersView.as_view(), name="riflers"),
    path('awps/', views.AWPsView.as_view(), name="awps"),
]
