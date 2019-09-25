from django.http import JsonResponse
from rest_framework.views import APIView

from rest_framework import viewsets
from .models import UserFrequency
import json

from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):

        # user = User.objects.get(pk=kwargs.get("pk"))
        # serializer = UserSerializer(user)

        # import ipdb; ipdb.set_trace()
        # user.nickname = data.get("nickname")
        # user.save()

        data = json.loads(request.body)
        User.objects.filter(pk=kwargs.get("pk")).update(**data)

        return Response()

        # import ipdb; ipdb.set_trace()



class UserFrequencyView(APIView):
  
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