from rest_framework.serializers import (
    ModelSerializer,
)

from promotions.models import  Promotion


class szPromotion(ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('name','imagebanner','datestart','dateend')