from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Manager(models.Model):
	class Meta:
		verbose_name = "Управляющий"
		verbose_name_plural = "Управляющие"

	name = models.CharField(max_length=100, verbose_name='Фамилия Имя Отчество')
	phone = PhoneNumberField(null=True, blank=False, unique=True, verbose_name='Контактный номер')
	email = models.EmailField(max_length = 254, null=True, blank=False, verbose_name='E-mail')
	comment = models.TextField(max_length=500, null=True, blank=False, verbose_name='Комментарий')

	def __str__(self):
		return self.name



class Hotel(models.Model):
	class Meta:
		verbose_name = "Отель"
		verbose_name_plural = "Отели"

	file = open(r'cities.txt', 'r', encoding='utf-8')
	text = file.readlines()
	file.close()
	cities = []
	for i in range(len(text)):
		if '\n' in text[i]:
			text[i] = text[i][:-1]
		cities.append((text[i], text[i]))
	cities = tuple(cities)

	name = models.CharField(max_length=200, verbose_name='Название отеля')
	#phone = models.CharField(max_length=100)
	manager = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name='ФИО управляющего')
	phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Контактный номер')
	location = models.CharField(max_length=200, verbose_name='Местоположение', choices=cities)
	description = models.TextField(max_length=500, verbose_name='Описание отеля')

	def __str__(self):
		return self.name