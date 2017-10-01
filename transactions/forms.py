import decimal
from django.forms import (
    ModelForm
    , CharField, EmailField, DecimalField, ImageField, FileField, ChoiceField, ModelChoiceField
    , TextInput, NumberInput, PasswordInput, FileInput, ClearableFileInput, Select
    , ValidationError
)
from django.contrib.auth.forms import UserCreationForm
from transactions.models import Transaction
from cards.models import Card

CHOICES_BANK = (
    ('BRI','BANK RI'),
    ('BM','BANK MANDIRI'),
    ('BCA','BANK CENTRAL ASIA'),
)

class PaymentForm(ModelForm):
    TransactionKey = CharField(
        required = True
    )
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
    tempMerchantBankName = ChoiceField(
        required = True,
        widget=Select(
            attrs={'class': 'form-control'
                , 'placeholder': 'Bank Penerima Pembayaran'}),
        choices = CHOICES_BANK,
    )
    tempMerchantBankAccount = CharField(
        required = True,
        widget=NumberInput(
            attrs={'class': 'form-control'
                , 'placeholder': 'Nomor Rekening Pembayaran'})
    )
    amount = DecimalField(
        widget=TextInput(
            attrs={'class': 'form-control'
                   ,'placeholder': 'Nilai Rupiah yang dibayarkan.'
                   ,'data-a-sep':"."
                   ,'data-a-dec':","})
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


    class Meta:
        model = Transaction
        fields = (
            'TransactionKey'
            , 'tempMerchantName'        , 'tempMerchantPhone'
            , 'tempMerchantBankName'    , 'tempMerchantBankAccount'
            , 'amount'                  ,'category'
            , 'invoice'                 ,'CardUsed'
        )

    def __init__(self, *args, **kwargs):
        self.payer = kwargs.pop('payer',None)
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['CardUsed'].queryset = Card.objects.filter(owner=self.payer)







