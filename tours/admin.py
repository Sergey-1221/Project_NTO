from django.contrib import admin

# Register your models here.
from .models import Hotel, Manager

admin.site.register(Hotel) 
admin.site.register(Manager) 