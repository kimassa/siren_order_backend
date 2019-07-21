from django.db import models


class User(models.Model):

      IS_SUPPLIER = 'SUPPLIER'
      IS_CUSTOMER = 'CUSTOMER'
      USER_CHOICES = [
        (IS_SUPPLIER, 'SUPPLIER'),
        (IS_CUSTOMER, 'CUSTOMER'),
      ]

      name = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      phone = models.CharField(max_length=40)
      password = models.CharField(max_length=200)
      is_supplier = models.CharField(max_length=20, choices=USER_CHOICES)

      class Meta:
          db_table='users'
      
      def __str__(self):
          return self.name


class UserFrequency(models.Model):
 
      special_drink = models.PositiveIntegerField(max_length=5)
      normal_drink = models.PositiveIntegerField(max_length=5)
      user_number = models.PositiveIntegerField(max_length=30)
      user = models.OneToOneField(User, on_delete=models.CASCADE)

      class Meta:
          db_table='users_frequencies'
      
      def __str__(self):
          return self.user.name