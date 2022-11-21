from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Hotel(models.Model):
	name = models.CharField(max_length=200)
	#phone = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	phone = PhoneNumberField(null=False, blank=False, unique=True)