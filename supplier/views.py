from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from .models import Supplier
from user.utils import login_required
from user.models import User
from .serializers import SupplierSerializer
from geopy.distance import distance
from rest_framework import viewsets


class SupplierAllView(viewsets.ViewSet):

    def list(self, request):

        data = Supplier.objects.all()
        serializer = SupplierSerializer(data, many=True)

        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):

        data = Supplier.objects.get(id=pk)
        serializer = SupplierSerializer(data)

        return JsonResponse(serializer.data, safe=False)


class SupplierDetailView(APIView):
    def get(self, request, pk):

        supplier = Supplier.objects.filter(id=pk)
        supplier_list = list(supplier.values())
              
        data_json = [ {
                'name' : d['name'],
                'supplier_id' : d['id'],
                'branch' : d['branch'],
                'address' : d['address'],
                'zipcode' : d['zipcode'],
                'phone' : d['phone'],
                'latitude': d['latitude'],
                'longitude' : d['longitude'],
                'img_src' : "https://s3-siren.s3.ap-northeast-2.amazonaws.com/samsung_starbucks.jpeg"
            } for d in supplier_list
        ]
        
        return JsonResponse(data_json, safe=False)            


class SupplierLocationView(APIView):
    def get(self, request):

        suppliers = Supplier.objects.all().values()
        # suppliers_list = list(suppliers)
        latitude = request.GET['lat']
        longitude = request.GET['lon']
        current_coord = (latitude, longitude)    

        data_json = [ {
            'distance' : distance(current_coord, (d['latitude'], d['longitude'])).m,
            'name' : d['name'],
            'supplier_id' : d['id'],
            'branch' : d['branch'],
            'address' : d['address'],
            'zipcode' : d['zipcode'],
            'phone' : d['phone'],
            'latitude': d['latitude'],
            'longitude' : d['longitude'],
        } for d in suppliers.iterator() ]

        sorted_list = sorted(data_json, key = lambda i: i['distance'])
        first_ten_list = sorted_list[:10]
        
        return JsonResponse(first_ten_list, safe=False)

class SupplierFavoriteView(APIView):

    @login_required
    def post(self, request, pk):

        supplier = get_object_or_404(Supplier, id=pk)
        user = get_object_or_404(User, id=request.user.id)

        if supplier.favorite.filter(id = request.user.id).exists():
                supplier.favorite.remove(user)
                return JsonResponse({'message':'favorited'}, status=200)
        else :
                supplier.favorite.add(user)
                return JsonResponse({'message':'Unfavorited'}, status=200)


# class FileView(APIView):
#
#     s3_client = boto3.client(
#         's3',
#         aws_access_key_id= my_settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key= my_settings.AWS_SECRET_ACCESS_KEY
#     )
#
#     def post(self, request):
#         file = request.FILES['filename']
#
#         self.s3_client.upload_fileobj(
#             file,
#             "s3-test-wecode",
#             file.name,
#             ExtraArgs={
#                 "ContentType": file.content_type
#             }
#         )
#
#         return HttpResponse(status= 200)