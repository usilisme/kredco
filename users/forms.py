from django.forms import (
    ModelForm, CharField, EmailField,ImageField, TextInput, PasswordInput
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import UserProfile


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class EditProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','nik')

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








