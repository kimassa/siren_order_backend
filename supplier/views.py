from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Supplier, Address
from django.core import serializers
import json
from geopy.distance import distance
from operator import itemgetter, attrgetter


class SupplierView(View):
    
    def get(self, request):
        data = Supplier.objects.all().values()
        data_list = list(data)

        data_json = [ {
            'name' : d['name'],
            'address' : d['address'],
            'phone' : d['phone'],
        } for d in data_list ]

        return JsonResponse(data_json, safe=False)


class SupplierLocationView(View):

    def get(self, request):
     
        suppliers = Supplier.objects.all()
        suppliers_list = list(suppliers)
        address = Address.objects.filter(supplier__in=suppliers).select_related()
        address_list = list(address)

        dictionary = dict(zip(suppliers_list, address_list))

        cities = {
            'vienna': (48.2083537, 16.3725042),
            'berlin': (52.5170365, 13.3888599),
            'sydney': (-33.8548157, 151.2164539),
            'madrid': (40.4167047, -3.7035825)
            }

        latitude = request.GET['lat']
        longitude = request.GET['lon']
        current_coord = (latitude, longitude)
        distance_list = []

        for shop, address in dictionary.items():
            longitude = address.longitude
            latitude = address.latitude
            coord = (longitude, latitude)
            shop_name = shop.name
            d = distance(current_coord, coord).m

            result = distance_list.append((shop_name, d))
        
        sorted_list = sorted(distance_list, key=itemgetter(1))
    
        return JsonResponse(sorted_list, safe=False)