
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from meiduo_mall_admin.utils.custom_pagination import MyPagination
from meiduo_mall_admin.serializers.admin_serializers import *
from meiduo_mall_admin.serializers.group_serializers import GroupModelSerializer, Group


class GroupSimpleListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class AdminModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminModelSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        # 过滤非管理员用户
        return self.queryset.filter(is_staff=True)


