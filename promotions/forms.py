from django.forms import ModelForm

from promotions.models import Promotion

class foPromotion (ModelForm):
    class Meta:
        model = Promotion
        fields = ('name','imagebanner','datestart','dateend')




