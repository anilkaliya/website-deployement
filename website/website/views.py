from django.urls import reverse
from django.conf.urls import url,include
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
class HomePage(TemplateView):
    template_name = "index.html"
class TestPage(TemplateView):
    template_name = 'test.html'

class Thanks(TemplateView):
    template_name='thanks.html'

class Aboutview(TemplateView):
    template_name='about.html'
