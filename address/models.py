from django.db import models

class Address(models.Model):
    zipcode = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    detail_address = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    class Meta:
        db_table='addresses'
    
    def __str__(self):
        return self.detail_address