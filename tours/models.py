from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Manager(models.Model):
	class Meta:
		verbose_name = "Контактное лицо"
		verbose_name_plural = "Контактные лица"

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
	manager = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name='ФИО управляющего')
	phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Контактный номер')
	location = models.CharField(max_length=200, verbose_name='Местоположение', choices=cities)
	description = models.TextField(max_length=500, verbose_name='Описание отеля')

	def __str__(self):
		return self.name

class Tours(models.Model):
	class Meta:
		verbose_name = "Тур"
		verbose_name_plural = "Туры"

	FOOD_TYPE = [
		("0","Без питания"), 
		("1","С завтраком"), 
		("2","3-х разовое")
	]

	hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, verbose_name='Отель')
	date_of_stay = models.DateField(null=True, auto_now = False, auto_now_add = False, verbose_name='Дата заезда')
	date_of_exit = models.DateField(null=True, auto_now=False, auto_now_add=False, verbose_name='Дата выезда')
	numbers_day = models.IntegerField(verbose_name='Количество дней')
	food = models.CharField(max_length=200, verbose_name='Вид питания', choices=FOOD_TYPE)
	price = models.FloatField(verbose_name='Стоимость тура')
	description = models.TextField(max_length=500, verbose_name='Описание тура')

	class Meta:
		verbose_name = "Тур"
		verbose_name_plural = "Туры"

	def Days_Nights(self):
		days = self.date_of_exit - self.date_of_stay
		nights = self.date_of_exit - self.date_of_stay
		print(type(days))
		return f"{days}\\{nights}"

	Days_Nights.short_description = 'Дней \\ Ночей'

class Client(models.Model):
	name = models.CharField(max_length=100, verbose_name='Клиент')
	contact_person = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name='Контактное лицо')
	options = (('Физическое лицо','Физическое лицо'),
	     ('Юридическое лицо', 'Юридическое лицо'))
	phone = PhoneNumberField(null=True, blank=False, unique=True, verbose_name='Контактный номер')
	option = models.CharField(max_length=100, verbose_name='Вид клиента', choices=options)

	class Meta:
		verbose_name = "Клиент"
		verbose_name_plural = "Клиенты"