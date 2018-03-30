from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from . import task6


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['khe'] = task6.khe.kkk("as", "gfg")
    lista = ["ajh", "asiinx", "aijic", "askcj", "iiwquhda"]

    return render_to_response('hello.html', {'context': context, 'lista': lista})
