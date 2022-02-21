from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm

def login_user(request):
    login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")

            else:
                return render(request, 'registration/login.html', {'login_form': login_form, 'login_error': True})

    context = {'login_form': login_form, 'login_error': False}
    return render(request, 'registration/login.html', context)

def register_user(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return redirect("/login/")

    else:
        register_form = RegisterForm()

    return render(request, 'registration/register.html', {'register_form': register_form})

def logout_user(request):
    logout(request)
    return redirect("/")
