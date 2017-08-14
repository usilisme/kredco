from django import forms
from django.contrib.auth.models import User
from kred.models import Payer,Card, Promo

class FormUser (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password',)

class FormPayer (forms.ModelForm):
    addrMail = forms.CharField(max_length=128,help_text="Mailing Address")
    class Meta:
        model = Payer
        fields = ('addrMail',)

class FormCard (forms.ModelForm):
    number = forms.CharField(max_length=128,help_text="Card Number")
    class Meta:
        model = Card
        fields = ('number',)




