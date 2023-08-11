from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisements

# Create your views here.

def index(request):
    # return HttpResponse('Успешно, молодец!!')
    advertisements = Advertisements.objects.all()
    context ={"advertisements": advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def placeadd(request):
    return render(request, 'advertisement-post.html')

def registrat(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profil(request):
    return render(request, 'profile.html')

