from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Hotel(models.Model):
	name = models.CharField(max_length=200)
	#phone = models.CharField(max_length=100)
	description = models.TextField(max_length=500, verbose_name='Описание отеля')
	phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Контактный номер')

class Company(models.Model):
	name = models.CharField(max_length=30)

class Product(models.Model):
	company = models.ForeignKey(Company, on_delete = models.CASCADE)
	name = models.CharField(max_length=30)
	price = models.IntegerField()