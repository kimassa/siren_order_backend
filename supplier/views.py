from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Supplier
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
        supplier_address = dict(zip(suppliers_list, address_list))

        latitude = request.GET['lat']
        longitude = request.GET['lon']
        current_coord = (latitude, longitude)
        distance_list = []

        for shop, address in supplier_address.items():
            longitude = address.longitude
            latitude = address.latitude
            coord = (longitude, latitude)
            shop_name = shop.name
            d = distance(current_coord, coord).m

            result = distance_list.append((shop_name, d))
        
        sorted_list = sorted(distance_list, key=itemgetter(1))
    
        return JsonResponse(sorted_list, safe=False)