from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Product
from django.core import serializers
import json

class AllProductView(View):
    
    def get(self, request):
        data = Product.objects.all().values()
        print(data)
        data_list = list(data)

        data_json = [ {
            'name' : d['name'],
            'menu_type' : d['menu_type'],
            'drink_type' : d['drink_type'],
            'drink_size' : d['drink_size'],
            'price' : d['price'],

        } for d in data_list ]

        return JsonResponse(data_json, safe=False)