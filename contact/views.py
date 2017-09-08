# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django import forms

# Create your views here.
class QueryForm(forms.ModelForm):

	class Meta:
		model = Query
		fields = ('name', 'email', 'phone_number', 'amount', 'text')


def main_page(request):
	form = QueryForm()
	return render(request, 'index.html', {'form': form})