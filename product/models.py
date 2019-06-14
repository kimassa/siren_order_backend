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

      SMALL = 'SM'
      TALL = 'TA'
      GRANDE = 'GR'
      VENTI = 'VE'
      SIZE_CHOICES = [
        (SMALL, 'Small'),
        (TALL, 'Tall'),
        (GRANDE, 'Grande'),
        (VENTI, 'Venti'),
      ]

      ICED = 'IC'
      HOT = 'HO'
      DRINK_CHOICES = [
        (ICED, 'Iced'),
        (HOT, 'Hot'),
      ]

      name = models.CharField(max_length=100)
      menu_type = models.CharField(max_length=20, choices=MENU_CHOICES)
      drink_type = models.CharField(max_length=10, choices=DRINK_CHOICES, null=True, blank=True)
      price = models.CharField(max_length=50)
      drink_size = models.CharField(max_length=10, choices=SIZE_CHOICES, null=True, blank=True)
      detail = models.CharField(max_length=100, null=True, blank=True)

      class Meta:
          db_table='products'
      
      def __str__(self):
          return self.name