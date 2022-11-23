from django.contrib import admin

# Register your models here.
from .models import Hotel, Manager, Tours, Client


admin.site.register(Client) 

@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ("hotel", "Days_Nights", "date_of_stay", "date_of_exit", "food", "price", "description")
    fields = "hotel", ("date_of_stay", "date_of_exit"), "food", "price", "description"

@admin.register(Hotel) 
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "manager", "phone", "location", "description")


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "comment")