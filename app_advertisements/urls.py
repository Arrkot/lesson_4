from django.urls import path
from .views import index, top_sellers, placeadd, registrat, login, profil

urlpatterns = [
    # path('user/', index),
    path('', index, name='main_page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', placeadd, name='place_an_add'),
    path('registr/', registrat, name='register'),
    path('login/', login, name='login'),
    path('profile/', profil, name='profile'),
    # path('#/', exitt, name='exit1')




]