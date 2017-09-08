# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.
@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'email', 'date_asked')