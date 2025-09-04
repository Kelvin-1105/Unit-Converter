from django.http import HttpResponse
from django.template import loader
from .models import Member

def length(request):
    template = loader.get_template('length.html')
    context = {
        'unit_measurements' : [
            'millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile'
        ]
    }
    return HttpResponse(template.render(context, request))

def weight(request):
    template = loader.get_template('weight.html')
    context = {
        'unit_measurements' : [
            'milligram', 'gram', 'kilogram', 'ounce', 'pound'
        ]
    }
    return HttpResponse(template.render(context, request))

def temperature(request):
    template = loader.get_template('temperature.html')
    context = {
        'unit_measurements' : [
            'Celsius', 'Fahrenheit', 'Kelvin'
        ]
    }
    return HttpResponse(template.render(context, request))

