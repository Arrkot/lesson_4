from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Advertisements
from .forms import AdvertisementsForm
from django.urls import reverse

# Create your views here.

def index(request):
    # return HttpResponse('Успешно, молодец!!')
    advertisements = Advertisements.objects.all()
    context ={"advertisements": advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def registrat(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profil(request):
    return render(request, 'profile.html')

# def advertisement_post(request):
#
#     form = AdvertisementsForm()
#     context = {"form": form}
#     return render(request, 'advertisement-post.html', context)


def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
        else:
            return render(request, 'advertisement-post.html', {'form': form})

    else:
        # advertisements = Advertisements.objects.all()
        context = {'form': AdvertisementsForm, 'var1': 'variable test'}
        # print(f'cont: {context}')
        return render(request, 'advertisement-post.html', context)


