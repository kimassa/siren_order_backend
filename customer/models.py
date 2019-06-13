from django.db import models


class Customer(models.Model):

      name = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      phone = models.CharField(max_length=40)
      detail = models.CharField(max_length=200)

      class Meta:
          db_table='customers'
      
      def __str__(self):
          return self.name