from django.forms import (
    ModelForm, CharField, EmailField, PasswordInput
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(ModelForm):
    password = CharField(
        widget= PasswordInput()
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password')






