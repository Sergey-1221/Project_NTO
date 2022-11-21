from django.contrib import admin

# Register your models here.
from .models import Hotel, Company, Product

admin.site.register(Hotel) 
admin.site.register(Company) 
admin.site.register(Product) 