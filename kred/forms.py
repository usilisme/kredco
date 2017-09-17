from django.forms import (
    CharField, EmailField, PasswordInput
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = CharField(
        max_length=30, required=False
    )
    email = EmailField(
        max_length=254, help_text='Required. Inform a valid email address.'
    )
    password1 = CharField(widget=PasswordInput())
    password2 = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )






