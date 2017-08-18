from rest_framework.serializers import (
    ModelSerializer,HyperlinkedModelSerializer, CharField, EmailField, ValidationError,
    PrimaryKeyRelatedField,
)

from cards.models import Card

class szListCard(ModelSerializer):
    class Meta:
        model = Card
        fields = ('id','number',)

class szGetCard (ModelSerializer):
    class Meta:
        model = Card
        fields = ('type','number','dtExpiry','addBill')

