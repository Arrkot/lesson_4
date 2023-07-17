from django.urls import path
from .views import bee

urlpatterns = [
    path('bee/', bee),
]