from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'username'})
    )
    password = forms.CharField(
        label="Password",
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'password'})
    )

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields= ["username", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        if User.objects.filter(username=cleaned_data["username"]).exists():
            raise ValidationError("This username already exists")
