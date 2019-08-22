from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

      nickname = models.CharField(max_length=100,blank=True)
      name = models.CharField(max_length=100,blank=True)
      phone = models.CharField(max_length=40,blank=True)

      class Meta:
          db_table='users'
      
      def __str__(self):
          return self.username

      # def save(self, *args, **kwargs):
      #     self.email = self.username
      #     super(User, self).save(*args, **kwargs)


class UserFrequency(models.Model):
 
      special_drink = models.PositiveIntegerField(max_length=5)
      normal_drink = models.PositiveIntegerField(max_length=5)
      user_number = models.PositiveIntegerField(max_length=30)
      user = models.OneToOneField(User, on_delete=models.CASCADE)

      class Meta:
          db_table='users_frequencies'
      
      def __str__(self):
          return self.user.name
