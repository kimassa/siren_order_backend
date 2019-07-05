import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.test import Client
from user.models import User
from order.models import Order


class AuthenticatedTest(TestCase):
    def test_order(self):
        self.assertEqual(1,1)
    
    # def test_order2(self):
    #     self.assertEqual(1,2)
    def test_api_authenticated(self):
        c = Client()
        # import pdb; pdb.set_trace()
        response = c.get('/order/orders/')
        self.assertEqual(response.status_code,401)


    def test_api_unauthenticated(self):
        c = Client()
        # import pdb; pdb.set_trace()
        response = c.get('/order/orders/')
        # print(response.status_code)
        self.assertEqual(response.status_code,401)


class OrderModelTest(TestCase):
     def test_create_order(self):
         self.assertEqual(Order.objects.count(),0)
         order = Order(user = user,total_price=10000,supplier=supplier,takeout = 'Take Out',date = datetime.now)
         self.assertEqual(Order.objects.count(),1)
         self.assertEqual(order.total_price,10000)

        #  user = models.ForeignKey(User, on_delete=models.CASCADE)
        #  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PAID)
        #  total_price = models.IntegerField()
        #  supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
        #  takeout = models.CharField(max_length=10, choices=TAKEOUT_CHOICES)
        #  date = models.DateTimeField()

