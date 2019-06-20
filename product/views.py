from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Product
from customer.models import Customer
from django.core import serializers
from customer.utils import login_required
import json

class ProductAllView(View):
    
    def get(self, request):
        data = Product.objects.all().values()
        data_list = list(data)

        data_json = [ {
            'name' : d['name'],
            'menu_type' : d['menu_type'],
            'drink_type' : d['drink_type'],
            'drink_size' : d['drink_size'],
            'price' : d['price'],

        } for d in data_list ]

        return JsonResponse(data_json, safe=False)

class ProductFavoriteView(View):

    @login_required
    def post(self, request, pk):

        product = get_object_or_404(Product, id=pk)
        customer = get_object_or_404(Customer, id=request.user.id)

        if product.favorite.filter(id = request.user.id).exists():
                product.favorite.remove(customer)
                return JsonResponse({'message':'favorited'}, status=200)
        else :
                product.favorite.add(customer)
                return JsonResponse({'message':'Unfavorited'}, status=200)

        