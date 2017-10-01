from django.contrib.auth.models import User
from django.forms import (
    ModelForm,
    CharField, EmailField,ImageField, ModelChoiceField,IntegerField,
    TextInput, NumberInput, PasswordInput, HiddenInput,
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator

from cards.models import Card


class CardCreateForm(ModelForm):
    number = CharField(validators=[MinLengthValidator(16)],
        widget=NumberInput(
            attrs={'pattern':'[0-9]*'
                ,'data-politespace':''
                ,'data-politespace-creditcard':''
                , 'data-politespace-creditcard-maxlength': ''
                ,'data-politespace-grouplength':'4,4,4,4'
                ,'class': 'form-control'
                ,'placeholder':'16 digit angka'
                   }
        )
    )
    ExpiryMonth = IntegerField(
        min_value=1, max_value=12,
        widget=NumberInput(
            attrs={'size':2
                   ,'placeholder':'MM'
                   }
        )
    )
    ExpiryYear = IntegerField(
        min_value=2017, max_value=2050,
        widget=NumberInput(
            attrs={
                'size':4
                , 'placeholder': 'YYYY'
            }
        )
    )

    owner = ModelChoiceField(
        queryset=User.objects.all(),
        widget=HiddenInput()
    )

    class Meta:
        model = Card
        fields = ('type','number','ExpiryMonth','ExpiryYear' ,'owner')

class CardDeleteForm(ModelForm):
    class Meta:
        model =Card
        fields = ('id',)