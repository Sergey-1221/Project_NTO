from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("tour_order", "price")

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("tour_order", "booking", "сlient", "payment_type", "price_tmp", "people", "price")
