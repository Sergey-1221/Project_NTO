from django.contrib import admin

# Register your models here.
from .models import Hotel, Manager, Tours

admin.register(Tours) 
@admin.register(Hotel) 
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "manager", "phone", "location", "description")


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "comment")