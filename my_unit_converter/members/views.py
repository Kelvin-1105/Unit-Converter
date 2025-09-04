from django.http import HttpResponse
from django.template import loader
from .models import Member

def length(request):
    template = loader.get_template('length.html')
    
    return HttpResponse(template.render())

def weight(request):
    template = loader.get_template('weight.html')
    return HttpResponse(template.render())

def temperature(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())

