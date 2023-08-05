from django.contrib import admin
from .models import Advertisements
# Register your models here.

class AdvertisementsAdmin(admin.ModelAdmin):
    # list_display = ['id', 'title', 'description', 'price', 'created_date', 'update_date', 'auction']
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction']
    list_filter = ['auction', 'create_at']

admin.site.register(Advertisements, AdvertisementsAdmin)

