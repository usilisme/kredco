# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from users.models import UserProfile

admin.site.register(UserProfile)
