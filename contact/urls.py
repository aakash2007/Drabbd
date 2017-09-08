from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	url(r'^$', views.main_page, name='index'),
	url(r'^what/$', TemplateView.as_view(template_name='what.html'), name='what'),
	url(r'^how/$', TemplateView.as_view(template_name='how.html'), name='how')
]