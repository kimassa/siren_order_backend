from django.db import models
from user.models import User
from supplier.models import Supplier
from product.models import Product

class Order(models.Model):
    PAID = 'PAID'
    ORDER_SEND = 'ORDER_SEND'
    ORDER_CONFIRMED = 'ORDER_CONFIRMED'
    ORDER_CANCELED = 'ORDER_CANCELED'
    PRODUCT_READY = 'PRODUCT_READY'
    STATUS_CHOICES = [
        (PAID, 'Paid'),
        (ORDER_SEND, 'Order Send'),
        (ORDER_CONFIRMED, 'Order Confirmed'),        
        (ORDER_CANCELED, 'Order Canceled'),
        (PRODUCT_READY, 'Product Ready'),
    ]

    EAT_IN = 'EAT_IN'
    TAKE_OUT = 'TAKE_OUT'
    TAKEOUT_CHOICES = [
        (EAT_IN, 'Eat In'),
        (TAKE_OUT, 'Take Out'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PAID)
    total_price = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    takeout = models.CharField(max_length=10, choices=TAKEOUT_CHOICES)
    date = models.DateTimeField()

    class Meta:
        db_table='orders'
        verbose_name='주문'
        verbose_name_plural='주문들'
    
    def __str__(self):
        return f"{self.user} {self.total_price}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    class Meta:
        db_table='orders_products'
    
    def __str__(self):
        return f"{self.id} {self.product} {self.quantity}"