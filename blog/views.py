#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    name = 'Zeeshan'
    html = "<html><body> hi this is %s.</body></html>" %name
    return HttpResponse(html)
