from django.urls import path

from . import views

urlpatterns = [
        path('', views.homepage, name="homepage"),
        path('knifes/', views.knifes, name="knifes"),
        path('gloves/', views.gloves, name="gloves"),
        path('pistols/', views.pistols, name="pistols"),
        path('riflers/', views.riflers, name="riflers"),
        path('awps/', views.awps, name="awps"),
]
