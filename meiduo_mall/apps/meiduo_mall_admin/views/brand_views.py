from rest_framework.viewsets import ModelViewSet

from meiduo_mall_admin.serializers.brand_serializers import *
from meiduo_mall_admin.utils.custom_pagination import MyPagination


class BrandModelViewSet(ModelViewSet):
    """商品品牌增删改查"""

    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    pagination_class = MyPagination

