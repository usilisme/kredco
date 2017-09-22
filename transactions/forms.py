from django.forms import (
    ModelForm
    , CharField, EmailField, DecimalField, ImageField, FileField
    , TextInput, NumberInput, PasswordInput, FileInput, ClearableFileInput
    , ValidationError
)
from django.contrib.auth.forms import UserCreationForm
from transactions.models import Transaction

class PaymentForm(ModelForm):
    TransactionKey = CharField()
    tempMerchantName = CharField(
        required = True,
        widget=TextInput(
            attrs={'class':'form-control'
                ,'placeholder':'Nama Lengkap Sesuai KTP'
                ,'hd':'True'})
    )
    tempMerchantPhone = CharField(
        widget=NumberInput(
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
    amount = DecimalField(
        widget=TextInput(
            attrs={'class': 'form-control'
                   ,'placeholder': 'Nilai Rupiah yang dibayarkan.'
                   ,'data-a-sep':","
                   ,'data-a-dec':"."})
    )
    category = CharField(
        widget=TextInput(
            attrs={'class': 'form-control'
                , 'placeholder': 'Tujuan Pembayaran'})
    )
    invoice = FileField(
        required=False,
        widget=FileInput(
            attrs={'class':'form-control'
                   ,'placeholder':'Upload Foto Invoice'
                   ,'required':'false'})
    )
    tempCardNumber = CharField(
        max_length=16,
        widget=TextInput(
            attrs={'class':'form-control'
                   ,'placeholder':'16-digit Nomor Kartu Kredit'})
    )
    tempCardOwnerName = CharField(
        widget=TextInput(
            attrs={'class': 'form-control'
                , 'placeholder': 'Nama pemegang Kartu Kredit'})
    )
    tempCardExpiryDate = CharField(
        max_length=5,
        widget=TextInput(
            attrs={'class': 'form-control'
                , 'placeholder': 'MM/YY'})
    )
    tempCVV = CharField(
        max_length=3,
        widget=TextInput(
            attrs={'class': 'form-control'
                , 'placeholder': 'CVV'})
    )

    class Meta:
        model = Transaction
        fields = (
            'TransactionKey'
            , 'tempMerchantName'        , 'tempMerchantPhone'
            , 'tempMerchantBankName'    , 'tempMerchantBankAccount'
            , 'amount'                  ,'category'
            , 'invoice'
            , 'tempCardNumber'
        )






