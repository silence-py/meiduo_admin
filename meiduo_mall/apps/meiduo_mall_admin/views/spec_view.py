

from rest_framework.viewsets import ModelViewSet
from meiduo_mall_admin.serializers.spec_serializer import *
from meiduo_mall_admin.utils.custom_pagination import MyPagination


class SPUSpecModelViewSet(ModelViewSet):

    queryset = SPUSpecification.objects.all()
    serializer_class = SpecDetailModelSerializer
    pagination_class = MyPagination
