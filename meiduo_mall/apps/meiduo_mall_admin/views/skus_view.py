from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

# from goods.models import SKU, GoodsCategory, SPU
from meiduo_mall_admin.utils.custom_pagination import MyPagination
from meiduo_mall_admin.serializers.skus_serializer import *


class SKUGoodsView(ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKUGoodModelSerializer

    pagination_class = MyPagination

    def get_queryset(self):
        # 获取查询参数
        keyword = self.request.query_params.get('keyword')
        # 判断是否有keyword
        if not keyword:
            return self.queryset

        # 过滤查询集
        return SKU.objects.filter(name__contains=keyword)


class GoodCategoryListView(ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodCategoryModelSerializer

    # 过滤查询集
    def get_queryset(self):
        # 获取所有三级分类, parent_id大于37的为三级分类
        return GoodsCategory.objects.filter(parent_id__gt=37)


class SPUNameListView(ListAPIView):
    queryset = SPU.objects.all()
    serializer_class = SPUNameModelSerializer


class SPUSpecOptView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecModelSerializer

    def get_queryset(self):
        # 获取路径参数pk
        spu_id = self.kwargs.get('pk')
        # 返回spu对应的查询集
        return SPUSpecification.objects.filter(spu_id=spu_id)