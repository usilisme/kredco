from rest_framework.serializers import (
    ModelSerializer,HyperlinkedModelSerializer, CharField, EmailField, ValidationError
)

from merchants.models import Merchant

class szListMerchant (ModelSerializer):
    class Meta:
        model = Merchant
        fields = ('name',)