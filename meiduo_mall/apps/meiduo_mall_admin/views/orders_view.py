from meiduo_mall_admin.serializers.order_serializers import *
from rest_framework.viewsets import ModelViewSet
from meiduo_mall_admin.utils.custom_pagination import MyPagination


class OrderModelViewSet(ModelViewSet):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderModelSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if not keyword:
            return self.queryset.all()

        return self.queryset.filter(order_id__contains=keyword)

    def get_serializer_class(self):
        # self.action属性可以获取当前视图的处理函数
        # 如果处理函数是list: 使用OrderModelSerializer序列化器
        # 如果处理函数是retrieve: 使用OrderDetailModelSerializer序列化器
        # 如果处理函数是update: 使用OrderDetailModelSerializer序列化器
        if self.action == 'list':
            return self.serializer_class
        if self.action == 'retrieve':
            return OrderDetailModelSerializer
        if self.action == 'partial_update':
            return OrderDetailModelSerializer
