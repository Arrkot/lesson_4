from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index1(request):
    return HttpResponse('домашка по 4-ому заданию')