# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models import (
    Model, CharField, ImageField, OneToOneField
)

upload_path = 'media/images/users/'

class UserProfile(Model):
    user = OneToOneField(User, related_name='profiles')
    nameFull = CharField(
        max_length=200,
        blank=True
    )
    nik = CharField( #Identification Number / Nomor Induk KTP
        max_length=20
    )
    livingAddress = CharField(max_length=10, null=True, blank=True)
    avatar = ImageField(
        upload_to=upload_path,
        blank=True
    )
    verificationImage1 = ImageField(
        upload_to=upload_path,
        blank=True
    )
    verificationImage2 = ImageField(
        upload_to=upload_path,
        blank=True
    )
    verificationImage3 = ImageField(
        upload_to=upload_path,
        blank=True
    )
    verificationImage4 = ImageField(
        upload_to=upload_path,
        blank=True
    )

    def __str__(self):
        return self.user.username
