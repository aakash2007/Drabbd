# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import CreateView
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from .models import *
from django import forms

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class MainView(CreateView):
	# form = QueryForm()
	# return render(request, 'index.html', {'form': form})
	model = Query
	fields = ['name', 'email', 'phone_number', 'amount', 'text']
	template_name = 'index.html'
	success_url = '.'
	def get(self, request, *args, **kwargs):
		return super(MainView, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		res = super(MainView, self).post(request, *args, **kwargs)
		return JsonResponse({'success' : 1})