from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import User
from django.core import serializers
import json, bcrypt, jwt, secrets
from siren_order.settings import siren_secret
from user.utils import login_required


# 회원가입
class UserSignUpView(View):
    def post(self, request):
        user_input = json.loads(request.body)
        if User.objects.filter(email=user_input['email']).exists():
                return JsonResponse({'success': False, 'message': 'email already exists'},status=409)

        else:
            password = bytes(user_input['password'], "utf-8")
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            User(
                name = user_input['name'],
                email = user_input['email'],
                phone = user_input['phone'],
                password = hashed_password.decode("UTF-8")
            ).save()

            return JsonResponse({'success': True, 'message': 'sign up success'},status=200)

# 로그인
class UserSignInView(View):
    def post(self, request):        
        user_input = json.loads(request.body)
        input_email = user_input["email"]
        input_password = user_input["password"]

        if User.objects.filter(email=user_input['email']).exists():
            password = bytes(user_input['password'], "utf-8")
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            user = User.objects.get(email=user_input['email'])
            encoded_jwt_id = jwt.encode({'id' : user.id}, siren_secret, algorithm='HS256')

            if bcrypt.checkpw(user_input['password'].encode("UTF-8"), user.password.encode("UTF-8")):
                return JsonResponse({"access_token" : encoded_jwt_id.decode("UTF-8")}, status=200)
            else:
                return JsonResponse({'success': False, 'message':'invalid password'},status=401)
        else:
            return JsonResponse({'success': False, 'message': 'email does not exist'},status=401)


  