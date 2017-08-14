from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    ModelSerializer,HyperlinkedModelSerializer, CharField, EmailField, ValidationError
)
from rest_framework import serializers
from django.contrib.auth.models import User
from kred.models import UserProfile,Payer,Payee,Card,Txn,Promo

User = get_user_model()

class szCrUser(ModelSerializer):
    email1 = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = ('username','email1','email2','password')
        extra_kwargs = {"password":{"write_only":True}}
    def validate_email1(self,value):
        data = self.get_initial()
        email2 = data.get('email2')
        email1 = value
        if email1 != email1:
            raise ValidationError ('Email confirmation does not match')
        u = User.objects.filter(email=email2)
        if u.exists():
            raise ValidationError('This email address has been used')
        return value
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email1']
        password = validated_data['password']
        user_obj = User(
            username = username, email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class szLoginUser(ModelSerializer):
    u_obj = None
    token = CharField(allow_blank=True,read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address',required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ('token','username','email', 'password')
        extra_kwargs = {"password": {"write_only": True}}
    def validate(self,data):
        email = data.get('email',None)
        username = data.get('username', None)
        password = data["password"]
        if not email and not username:
            raise ValidationError('A username or email is required to login')
        u = User.objects.filter(
            Q(email=email) | Q(username=username)
        ).distinct()
        u = u.exclude(email__iexact="")
        if u.exists() and u.count()==1:
            u_obj = u.first()
        else:
            raise ValidationError('Username or email is not valid')

        if u_obj:
            if not u_obj.check_password(password):
                raise ValidationError("Incorrect credentials. Please try again.")
        data["token"] = "RANDOM_TOKEN"
        return data

class szUser(HyperlinkedModelSerializer):
    #cards = serializers.HyperlinkedRelatedField(many=True,view_name='card-detail',read_only=True)
    def create(self,validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class szUserProfile(HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('nameFull','nik','avatar')

class szPayer(HyperlinkedModelSerializer):
    class Meta:
        model = Payer

class szPayee(HyperlinkedModelSerializer):
    class Meta:
        model = Payee

class szCard(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Card
        fields = ('owner','number')

class szTxn(HyperlinkedModelSerializer):
    class Meta:
        model = Txn
        fields = ('TxnKey','amount')

class szPromo(HyperlinkedModelSerializer):
    class Meta:
        model = Promo
        fields = ('name','imgBanner','dateFr','dateTo')