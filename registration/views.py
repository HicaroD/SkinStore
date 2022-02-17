from django.shortcuts import render

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    return render(request, 'registration/register.html')
