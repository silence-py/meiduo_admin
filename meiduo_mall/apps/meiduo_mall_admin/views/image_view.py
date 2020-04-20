
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from meiduo_mall_admin.serializers.image_serializer import *
from meiduo_mall_admin.utils.custom_pagination import MyPagination


class SKUDetailListView(ListAPIView):
    queryset = SKU.objects.all()
    serializer_class = SKUDetailModelSerializer


class ImageModelViewSet(ModelViewSet):
    queryset = SKUImage.objects.all()
    serializer_class = ImageModelSerializer
    pagination_class = MyPagination
