from django.db import models
from user.models import User
from versatileimagefield.fields import VersatileImageField



class Product(models.Model):
      DRINK = 'drink'
      FOOD = 'food'

      MENU_CHOICES = [
        (DRINK, 'Drink'),
        (FOOD, 'Bakery'),
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
      menu_category = models.CharField(max_length=20)
      drink_type = models.CharField(max_length=10, choices=DRINK_CHOICES, null=True, blank=True)
      drink_size = models.CharField(max_length=10, choices=SIZE_CHOICES, null=True, blank=True)
      price = models.CharField(max_length=50)
      detail = models.CharField(max_length=100, null=True, blank=True)
      favorite = models.ManyToManyField(User, related_name='Product_favorite', blank=True)
      image = VersatileImageField(
          'Image',
          upload_to='images/product/',
          null=True, blank=True
      )

      class Meta:
          db_table='products'
      
      def __str__(self):
          return self.name

class ProductImage(models.Model):
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      image = models.TextField()
      status = models.BooleanField()
      created = models.DateTimeField(auto_now_add=True)
      added_by = models.ForeignKey(User, on_delete=models.CASCADE)

      class Meta:
          db_table='product_images'
      def __str__(self):
          return self.product
