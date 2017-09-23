from django.forms import (
    ModelForm, CharField, EmailField,ImageField,
    TextInput, PasswordInput
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.forms import EditProfileForm
from users.models import UserProfile
from merchants.models import Merchant

class BeMerchantForm(EditProfileForm):
    class Meta:
        model = UserProfile
        fields = ('phone','nik', )
    def __init__(self, *args, **kwargs):
        self.isSeller = True

class CreateShopForm(ModelForm):
    class Meta:
        model = Merchant
        fields = ('name', )








