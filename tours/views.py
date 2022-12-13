from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Tour_order
import json

# Create your views here.
def get_total_price(request, id_people):
	price = sum(Tour.total_price() for Tour in Tour_order.objects.filter(сlient=int(id_people)))
	json_data = {"id": price}
	json_data = json.dumps(json_data)
	return HttpResponse(json_data, content_type="application/json")

