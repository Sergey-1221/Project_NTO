from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Hotel(models.Model):
	name = models.CharField(max_length=200)
	#phone = models.CharField(max_length=100)
	description = models.TextField(max_length=500, verbose_name='Описание отеля')
	phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Контактный номер')

	# file = open(r'C:\Users\carma\Desktop\python_dir\add_info\mysite\cities.txt', 'r', encoding='utf-8')
	# text = file.readlines()
	# file.close()
	# cities = []
	# for i in range(len(text)):
	# 	if '\n' in text[i]:
	# 		text[i] = text[i][:-1]
	# 	cities.append((text[i], text[i]))
	# cities = tuple(cities)
	# managers = (('1', 'Иванов Иван Викторович'),
	# 			('2', 'Петров Вадим Алексеевич'),
	# 			('3', 'Сидоров Андрей Васильевич'))
	# name_hotel = models.CharField(max_length=200, verbose_name='название отеля')
	# location = models.CharField(max_length=200, verbose_name='Местоположение', choices=cities)
	# phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Контактный номер')
	# manager = models.CharField(max_length=100, verbose_name='Управляющий', choices=managers)
	# description = models.TextField(max_length=500, verbose_name='Описание')
	#
	# def __str__(self):
	# 	return self.name_hotel
	#
	# class Meta:
	# 	verbose_name = 'Отель'
	# 	verbose_name_plural = 'Отель'
	# 	ordering = ['name_hotel']

class Company(models.Model):
	name = models.CharField(max_length=30)

class Product(models.Model):
	company = models.ForeignKey(Company, on_delete = models.CASCADE)
	name = models.CharField(max_length=30)
	price = models.IntegerField()