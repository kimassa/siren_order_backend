from django.shortcuts import render
from .models import Order, OrderProduct
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core import serializers
from customer.utils import login_required
from .models import Order, OrderProduct
from supplier.models import Supplier
from product.models import Product
from datetime import datetime
from django.db import transaction
import json

class OrderView(View):
    
    @transaction.atomic
    @login_required
    def post(self, request):
        front_inputs = json.loads(request.body)

        order = Order(
                customer_id = request.user.id,
                status = front_inputs['status'],
                total_price = front_inputs['total_price'],
                supplier = Supplier.objects.get(id = front_inputs['branch_id']),
                takeout = front_inputs['takeout_option'],
                date = datetime.now()
            )
        
        order.save()

        for product_id, product_quantity in front_inputs['orders'].items():
            OrderProduct(
                order = Order.objects.get(id = order.id),
                product = Product.objects.get(id = product_id),
                quantity = product_quantity
            ).save()

        return JsonResponse({'success': True, 'message': 'your order has been placed'},status=200)