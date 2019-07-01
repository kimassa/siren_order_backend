from django.shortcuts import render
from .models import Order, OrderProduct
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core import serializers
from user.utils import login_required
from .models import Order, OrderProduct
from supplier.models import Supplier
from product.models import Product
from user.models import User
from datetime import datetime
from django.db import transaction
import json

class OrderView(View):
    
    @transaction.atomic
    @login_required
    def post(self, request):
        front_inputs = json.loads(request.body)

        order = Order(
                user_id = request.user.id,
                status = "PAID",
                total_price = front_inputs['total_price'],
                supplier = Supplier.objects.get(id = front_inputs['branch_id']),
                takeout = front_inputs['takeout_option'],
                date = datetime.now()
            )
        
        order.save()

        for product_id, product_quantity in front_inputs['orders'].items():
            print(product_id)
            print(product_quantity)

            OrderProduct(
                order = Order.objects.get(id = order.id),
                product = Product.objects.get(id = product_id),
                quantity = product_quantity
            ).save()

        return JsonResponse({'success': True, 'message': 'your order has been placed'},status=200)

class OrderStatusView(View):
    @login_required
    def get(self, request):
        user = request.user
        data = Order.objects.all().values()
     
        data_json = [ {
            '고객명' : d['user_id'],
            '주문상태' : d['status'],
            '주문금액' : d['total_price'],
            '지점명' : d['supplier_id'],
            '테이크아웃여부' : d['takeout'],
            '주문일시' : d['date'],
        } for d in data.iterator()]

        return JsonResponse(data_json, safe=False)

    @login_required
    def post(self, request):
        front_inputs = json.loads(request.body)
        Order.objects.filter(pk=front_inputs['order_id']).update(status=front_inputs['status'])
        return JsonResponse({'success': True, 'message': 'your product is ready now.'},status=200)
