from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bee(request):
    # return HttpResponse('домашка по 4-ому заданию')
    return render(request, 'bee.html')