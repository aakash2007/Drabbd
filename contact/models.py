# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.

class Query(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	email_regex = RegexValidator(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Invalid Email Format")
	email = models.CharField(max_length=200 ,validators=[email_regex], null=False, blank=False)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=200, validators=[phone_regex], null=False, blank=False)
	amount = models.CharField(max_length=20, blank=False, null=False)
	text = models.TextField(null=False, blank=False, default='')
	date_asked = models.DateTimeField('Date Asked', blank=True)
	
	def save(self, *args, **kwargs):
		if self.date_asked is None:
			self.date_asked = timezone.now()

		return super(Query, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Query'
		verbose_name_plural = 'Queries'

	def __str__(self):
		return self.name