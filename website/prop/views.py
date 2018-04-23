from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from . import models
from prop.models import proper
import django_filters
from .filter import UserFilter

class Propercreateview(CreateView):
    fields=('location','price','area')
    model=models.proper

def propertyfromchandigarh(request):
    properties=proper.objects.filter(location__iexact='chandigarh').order_by('price')
    return render(request,'prop/chandigarh.html',{'properties':properties})

def propertyfrommohali(request):
    properties=proper.objects.filter(location__iexact='mohali').order_by('price')
    return render(request,'prop/mohali.html',{'properties':properties})

def propertyfromkharar(request):
    properties=proper.objects.filter(location__iexact='kharar').order_by('price')
    return render(request,'prop/kharar.html',{'properties':properties})



def search(request):
    property = proper.objects.all()
    property_filter = UserFilter(request.GET, queryset=property)
    return render(request, 'prop/user_list.html', {'filter': property_filter})
