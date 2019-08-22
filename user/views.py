from django.http import JsonResponse
from django.views import View

from .models import UserFrequency
import json




class UserFrequencyView(View):
  
    def get(self, request, pk):
        user_frequency = UserFrequency.objects.filter(user_id=pk).values()
        data_json = [ {
            'user_id' : d['user_id'],
            'user_number' : d['user_number'],
            'special_drink' : d['special_drink'],
            'normal_drink' : d['normal_drink']
        } for d in user_frequency.iterator() ]
        
        return JsonResponse(data_json, safe=False)

    def post(self, request, pk):

        # 보내기 받기

        user_frequency = UserFrequency.objects.filter(user_id=pk).values()      

        user_input = json.loads(request.body)
        input_special = user_input["special_drink"]
        input_special = user_input["normal_drink"]

        return JsonResponse(user_frequency, safe=False)