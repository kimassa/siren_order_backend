from django.db import models
from user.models import User
from supplier.models import Supplier
from product.models import Product
from django.http import JsonResponse, HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=PAID)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    takeout = models.CharField(max_length=10, choices=TAKEOUT_CHOICES)
    date = models.DateTimeField()

    class Meta:
        db_table = 'orders'
        # verbose_name='주문'
        # verbose_name_plural='주문들'

    def __str__(self):
        return f"{self.user} {self.status}"


    def add_product(self, product_id, product_quantity):
        order_product = OrderProduct(
            order=self,
            product=Product.objects.get(id=product_id),
            quantity=product_quantity,
        )
        order_product.save()
        OrderProduct.sum_price(order_product)

    def total_price(self):

        total_price = 0

        for ordered_product in self.orderproduct_set.all():
            print(ordered_product)
            total_price += int(ordered_product.price)

        return total_price

    def display_order_product(self):
        products_list = []

        for ordered_product in self.orderproduct_set.all():
            products_list.append(ordered_product)

        return products_list

    def send_notification(self):
        return True

    def body(self):

        data_json = {
            self.user,
            self.supplier,
            self.date,
            self.orderproduct_set.all()
        }
        return data_json




# @receiver(post_save, sender=Order)
# def order_post_save(sender, **kwargs):
#     import ipdb; ipdb.set_trace();
#     pass


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'orders_products'

    def __str__(self):
        return f"{self.product} {self.quantity}"

    def sum_price(self):
        self.price = int(self.product.price) * self.quantity
        self.save()

    def fetch_price(self):
        # 주문이 발생하면 현재가격을 불러와 이력을 남긴다
        pass
