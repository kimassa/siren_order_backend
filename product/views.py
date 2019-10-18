from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from user.models import User
from user.utils import login_required


class ProductAllView(APIView):
    
    def get(self, request):

        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)

        return JsonResponse(serializer.data, safe=False)


class ProductFavoriteView(APIView):

    @login_required
    def post(self, request, pk):

        product = get_object_or_404(Product, id=pk)
        user = get_object_or_404(User, id=request.user.id)

        if product.favorite.filter(id = request.user.id).exists():
            product.favorite.remove(user)
            return JsonResponse({'message':'favorited'}, status=200)
        else:
            product.favorite.add(user)
            return JsonResponse({'message':'Unfavorited'}, status=200)