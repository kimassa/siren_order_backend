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
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    takeout = models.CharField(max_length=10, choices=TAKEOUT_CHOICES)
    date = models.DateTimeField()

    class Meta:
        db_table='orders'
        verbose_name='주문'
        verbose_name_plural='주문들'
    
    def __str__(self):
        return f"{self.user} {self.status}"

    def add_product(self, product_id, product_quantity):
        order_product = OrderProduct(
                order = self,
                product = Product.objects.get(id = product_id),
                quantity = product_quantity
            )
        order_product.save()

    def display_order_product(self):
        ops = []

        for op in self.orderproduct_set.all():
            ops.append(op)
        
        return ops
        # return f"{self.product} {self.quantity}"



class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table='orders_products'
    
    def __str__(self):
        return f"{self.product} {self.quantity}"

    def total_price():
        return self.price * self.quantity

    def fetch_price():
        # 주문이 발생하면 현재가격을 불러와 이력을 남긴다
        pass
