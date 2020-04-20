from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from meiduo_mall_admin.serializers.channel_serializers import *
from meiduo_mall_admin.utils.custom_pagination import MyPagination
from meiduo_mall_admin.serializers.skus_serializer import GoodsCategory, GoodCategoryModelSerializer


class GoodCategoryListView(ListAPIView):
    """序列化返回商品一级类别"""
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodCategoryModelSerializer

    def get_queryset(self):
        # 过滤返回商品一级类别
        return self.queryset.filter(parent=None)


class GoodChannelModelListView(ListAPIView):
    """序列化返回商品频道"""
    queryset = GoodsChannelGroup.objects.all()
    serializer_class = ChannelGroupModelSerializer


class ChannelModelViewSet(ModelViewSet):
    # 商品频道增删改查

    queryset = GoodsChannel.objects.all()
    serializer_class = ChannelModelSerializer
    pagination_class = MyPagination
