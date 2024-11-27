from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=255)
    birth_date = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'birth_date', 'password1', 'password2']
