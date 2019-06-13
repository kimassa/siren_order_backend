from django.db import models

class Product(models.Model):
      DRINK = 'DR'
      ICECREAM = 'IC'
      SANDWICH = 'SW'
      BAKERY = 'BK'

      MENU_CHOICES = [
        (DRINK, 'Drink'),
        (ICECREAM, 'Ice Cream'),
        (SANDWICH, 'Sandwich'),
        (BAKERY, 'Bakery'),
      ]
      
      name = models.CharField(max_length=100)
      menu_type = models.CharField(max_length=20, choices=MENU_CHOICES)
      price = models.CharField(max_length=50)
      detail = models.CharField(max_length=100)

      class Meta:
          db_table='products'
      
      def __str__(self):
          return self.name