from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from meiduo_mall_admin.serializers.perm_serializers import *
from meiduo_mall_admin.utils.custom_pagination import MyPagination


class ContentTypeModelViewSet(ListAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer


class PermModelViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermModelSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        return self.queryset.order_by('id')
