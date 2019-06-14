from django.db import models
from address.models import Address

class Supplier(models.Model):
    name = models.CharField(max_length=40)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=40)

    class Meta:
        db_table='suppliers'

    def __str__(self):
        return self.name