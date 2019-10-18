from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from user.models import User
from user.utils import login_required
import json


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
        else :
                product.favorite.add(user)
                return JsonResponse({'message':'Unfavorited'}, status=200)


class ProductCreateView(APIView):

    @login_required
    def post(self, request):
        user = request.user
        property_get = request.POST

        if user.is_host:
            return JsonResponse({'message':'숙소가 이미 존재합니다.'}, status=400)
        else:
            try:
                new_property = Property(
                                name        = property_get.get('property_name'),
                                description = property_get.get('description'),
                                address1    = property_get.get('address1'),
                                address2    = property_get.get('address2',None),
                                postal      = property_get.get('postal'),
                                max_people  = property_get.get('max_people'),
                                price       = property_get.get('price'),
                                user_id     = user.id
                        )
                new_property.save()
                user.is_host = True
                user.save()

            except Exception as e:
                logger.exception(e)
                return JsonResponse({'message':'숙소저장 시 오류가 생겼습니다.'}, status=400)

        self.photos_to_aws(request, new_property.id)

        data = {
                'property_id': new_property.id,
                'message':'성공적으로 숙소가 등록되었습니다.' 
        }
        return JsonResponse(data, status=200)
        
    def photos_to_aws(self, request, property_id):

        s3_client = boto3.client(
            's3',
            aws_access_key_id     = my_settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = my_settings.AWS_SECRET_ACCESS_KEY
        )
        
        for key, image in request.FILES.items():
            extension = image.name.split('.')[-1]
            file_name = f"{uuid.uuid4()}.{extension}" 
            test = s3_client.upload_fileobj(
                image,
                "minibnb-test",
                file_name,
                ExtraArgs={
                    'ContentType': image.content_type
                }
            
            )
            new_image = Image(
                image    = "https://s3.ap-northeast-2.amazonaws.com/minibnb-test/"+file_name,
                added_by = request.user,
                property_id = property_id,
                status = True
            )
            new_image.save()


class ProductDeleteView(APIView):
    
    @login_required
    def post(self, request):
        user = request.user
        property_get = json.loads(request.body)
        if user.is_host:
            Property.objects.get(id=property_get['property_id']).delete()
            user.is_host = False
            user.save()
            return JsonResponse({'message':'숙소가 성공적으로 지워졌습니다'}, status=200)
        else:
            return JsonResponse({'message':'숙소가 존재하지 않습니다.'}, status=400)
