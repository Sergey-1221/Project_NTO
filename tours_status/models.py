from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html

from tours.models import Tour_order
# Create your models here.

class Payment(models.Model):
	class Meta:
		verbose_name = "Оплата тура"
		verbose_name_plural = "Оплаты туров"

	tour_order = models.OneToOneField(Tour_order, on_delete = models.CASCADE, primary_key = True, related_name="+", verbose_name='Заказ')
	def price(self):
		return self.tour_order.total_price()

	date = models.DateTimeField(auto_now=True, verbose_name='Дата')
	price.short_description = 'Стоимость'

	def __str__(self):
		return f"{self.tour_order}"


	"""
	def __str__(self):
		return self.name
	"""
class Sale(models.Model):
	class Meta:
		verbose_name = "Продажа тура"
		verbose_name_plural = "Продажи туров"

	tour_order = models.OneToOneField(Payment, on_delete = models.CASCADE, primary_key = True, related_name="+", verbose_name='Заказ')
	booking_type = [
		("Да","Да"),
		("Нет","Нет")
	]
	booking = models.CharField(max_length=100, verbose_name='Бронь номеров', choices=booking_type)

	date = models.DateTimeField(auto_now=True, verbose_name='Дата')

	def сlient(self):
		return self.tour_order.tour_order.сlient
	сlient.short_description = 'Клиент'

	def payment_type(self):
		return self.tour_order.tour_order.payment
	payment_type.short_description = 'Вид оплаты'

	def price_tmp(self):
		return self.tour_order.tour_order.price_tmp
	price_tmp.short_description = 'Цена'

	def people(self):
		return self.tour_order.tour_order.people
	people.short_description = 'Количество человек'

	def price(self):
		return self.tour_order.price()
	price.short_description = 'Стоимость'


	def save(self, *args, **kwargs):
		tour = Tour_order.objects.get(id=self.tour_order.tour_order.id)
		tour.status = "Завершен"
		tour.save()
		super(Sale, self).save(*args, **kwargs)

	def __str__(self):
		return f"{self.tour_order}"