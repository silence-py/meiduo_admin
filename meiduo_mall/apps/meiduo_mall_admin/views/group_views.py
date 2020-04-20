from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from meiduo_mall_admin.serializers.group_serializers import *
from meiduo_mall_admin.utils.custom_pagination import MyPagination
from meiduo_mall_admin.serializers.perm_serializers import PermModelSerializer, Permission


class PermSimpleListView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermModelSerializer


class GroupModelViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        return self.queryset.order_by('id')
