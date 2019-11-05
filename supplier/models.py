from django.db import models
from user.models import User
from product.models import Product


class Supplier(models.Model):
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    phone = models.CharField(max_length=40, blank=True)
    owner = models.ForeignKey(User, blank=True, null=True, related_name='owner', on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, related_name='manager', on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name='Supplier_favorite', blank=True)
    products = models.ManyToManyField(Product, related_name='supplier_product', blank=True)

    class Meta:
        db_table='suppliers'

    def products_count(self):
        return self.products.count()

    def __str__(self):
        return self.branch
