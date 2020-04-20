

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
# from goods.models import SPU
from meiduo_mall_admin.serializers.spus_serializer import *
from meiduo_mall_admin.utils.custom_pagination import MyPagination
from goods.models import GoodsCategory
from meiduo_mall_admin.serializers.skus_serializer import GoodCategoryModelSerializer


class BrandDetailListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailModelSerializer


class SPUDetailModelViewSet(ModelViewSet):
    queryset = SPU.objects.all()
    serializer_class = SPUDetailModelSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if not keyword:
            return self.queryset

        return self.queryset.filter(name__contains=keyword)


class GoodCategoryListView(ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodCategoryModelSerializer

    def get_queryset(self):
        # 获取父级类别id
        cat_id = self.kwargs.get('pk')
        if cat_id:
            # 过滤二,三级分类
            return self.queryset.filter(parent_id=cat_id)

        # 过滤一级分类
        return self.queryset.filter(parent=None)