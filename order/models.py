from django.db import models
from customer.models import Customer
from supplier.models import Supplier
from product.models import Product


class OrderCustomerProductSupplier(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        db_table='orders'
    
    def __str__(self):
        return self.pk