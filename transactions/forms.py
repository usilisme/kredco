from django.forms import (
    ModelForm
    , CharField, EmailField, DecimalField, ImageField
    , TextInput, NumberInput, PasswordInput, ValidationError
)
from django.contrib.auth.forms import UserCreationForm
from transactions.models import Transaction

class PaymentForm(ModelForm):
    tempMerchantName = CharField(
        widget=TextInput(
            attrs={'class':'form-control'
                ,'placeholder':'Nama Lengkap Sesuai KTP'})
    )
    tempMerchantPhone = CharField(
        widget=TextInput(
            attrs={'class': 'form-control'
                , 'placeholder': 'HP atau Telepon Rumah yang dapat dihubungi'})
    )
    tempMerchantBankName = CharField(
        widget=TextInput(
            attrs={'class': 'form-control'
                , 'placeholder': 'Bank Penerima Pembayaran'})
    )
    tempMerchantBankAccount = CharField(
        widget=TextInput(
            attrs={'class': 'form-control'
                , 'placeholder': 'Nomor Rekening Pembayaran'})
    )

    amount = CharField()
    category = CharField()
    invoice = CharField()

    tempCardNumber = CharField()
    tempCardOwnerName = CharField()
    tempCardExpiryDate = CharField()
    tempCardCVV = CharField()

    def clean_tempMerchantName(self):
        tempMerchantName = self.cleaned_data['tempMerchantName']
        if tempMerchantName == 'a':
            raise ValidationError("Apa Ini!")
        return tempMerchantName

    class Meta:
        model = Transaction
        fields = ('tmpMchntName', 'tmpMchntPhon'
                  , 'tmpMchntAcctNm', 'tmpMchntAcctNo'
                  )






