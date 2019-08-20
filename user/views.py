from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.views import APIView

from .models import User, UserFrequency
from django.core import serializers
import json, bcrypt, jwt, secrets
from user.utils import login_required

from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token


class UserSignUpView(APIView):

    def post(self, request):
        user_input = json.loads(request.body)

        User.objects.create_user(
                user_input['email'],
                password=user_input['password'],
                nickname=user_input['nickname'],
        ).save()

        return JsonResponse({"message":"201 OK"}, status=201)

class UserSignInView(APIView):

    def post(self, request):
        user_input = json.loads(request.body)

        email = user_input['email']
        password = user_input['password']


        user = authenticate(request, username=email, password=password)

        token = Token.objects.create(user=user)

        if user is not None:
            login(request, user)
            return JsonResponse({"message":"200 OK", "token":token.key},status=200)
        else:
            return JsonResponse({"message":"401 FAIL"},status=401)


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