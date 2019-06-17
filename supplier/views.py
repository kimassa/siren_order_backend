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
                'branch' : d['branch'],
                'address' : d['address'],
                'zipcode' : d['zipcode'],
                'phone' : d['phone'],
                'latitude': d['latitude'],
                'longitude' : d['longitude']
            } for d in data_list ]

            return JsonResponse(data_json, safe=False)


class SupplierLocationView(View):

    def get(self, request):

        suppliers = Supplier.objects.all().values()
        suppliers_list = list(suppliers)
        latitude = request.GET['lat']
        longitude = request.GET['lon']
        current_coord = (latitude, longitude)
        distance_list = []
        print(suppliers)
        print(suppliers_list)

        for supplier in suppliers_list:
            # address = supplier.address
            longitude = supplier['longitude']
            latitude = supplier['latitude']
            coord = (latitude, longitude)
            branch_name = supplier['branch']
            distance_result = distance(current_coord, coord).m

            result = distance_list.append((branch_name, distance_result))
            # print(result)

            data_json = [ {
                'name' : d['name'],
                'branch' : d['branch'],
                'address' : d['address'],
                'zipcode' : d['zipcode'],
                'phone' : d['phone'],
                'distance' : distance_result,
                'latitude': d['latitude'],
                'longitude' : d['longitude']
            } for d in suppliers_list ]

        sorted_list = sorted(distance_list, key=lambda d: d[1])
        return JsonResponse(data_json, safe=False)