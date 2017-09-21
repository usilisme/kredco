from django.forms import (
    ModelForm, CharField, EmailField, TextInput, PasswordInput
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(ModelForm):
    username = CharField(
        widget=TextInput(attrs={'class':'form-control','placeholder':'Username'})
    )
    email = CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    password = CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserForm(ModelForm):
    password = CharField(
        widget= PasswordInput()
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password')






