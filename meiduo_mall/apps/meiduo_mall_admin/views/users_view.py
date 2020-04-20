from rest_framework.generics import ListAPIView, CreateAPIView
from users.models import *

from meiduo_mall_admin.utils.custom_pagination import MyPagination
from meiduo_mall_admin.serializers.users_serializer import *


class UserListCreateView(ListAPIView, CreateAPIView):

    # 指定查询集
    queryset = User.objects.all()
    # 指定序列化模型类
    serializer_class = UserListCreateModelSerializer
    # 指定分页器
    pagination_class = MyPagination

    def get_queryset(self):

        # 获取查询参数
        keyword = self.request.query_params.get('keyword')

        # 如果获取不到keyword默认显示所有用户
        if not keyword:
            return self.queryset

        # 查询用户
        user = self.queryset.filter(username__contains=keyword)

        # 返回序列化对象
        return user


