
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from meiduo_mall_admin.serializers.spec_opt_serializer import *
from meiduo_mall_admin.utils.custom_pagination import MyPagination


class SpecListView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecModelSerializer


class SpecOptModelViewSet(ModelViewSet):
    queryset = SpecificationOption.objects.all()
    serializer_class = SpecOptModelSerializer
    pagination_class = MyPagination

