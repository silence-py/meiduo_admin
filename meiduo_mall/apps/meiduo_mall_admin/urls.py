from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter

from .views import index_view, users_view
from .views import skus_view, spus_view, spec_view, spec_opt_view, image_view, channel_views, brand_views
from .views import orders_view, perm_views, group_views, admin_views

urlpatterns = [
    # 用户认证
    url(r'^authorizations/$', obtain_jwt_token),

    # 总用户量
    url(r'^statistical/total_count/$', index_view.UserTotalView.as_view()),

    # 日增用户
    url(r'^statistical/day_increment/$', index_view.DayIncreaseUserView.as_view()),

    # 日活跃用户
    url(r'^statistical/day_active/$', index_view.DayActiveUserView.as_view()),

    # 日订单量
    url(r'^statistical/day_orders/$', index_view.DayOrderView.as_view()),

    # 月增用户
    url(r'^statistical/month_increment/$', index_view.MonthIncreaseUserView.as_view()),

    # 日商品类别访问
    url(r'^statistical/goods_day_views/$', index_view.DayGoodVisitView.as_view()),

    # 查询新增超级管理员用户
    url(r'^users/$', users_view.UserListCreateView.as_view()),

    # 新增sku-获取三级商品分类
    url(r'^skus/categories/$', skus_view.GoodCategoryListView.as_view()),

    # 新增sku-获取SPU名称
    url(r'^goods/simple/$', skus_view.SPUNameListView.as_view()),

    # 新增sku-获取SPU名称的规格和选项
    url(r'^goods/(?P<pk>\d+)/specs/$', skus_view.SPUSpecOptView.as_view()),

    # 新增spu-获取所有品牌名称
    url(r'^goods/brands/simple/$', spus_view.BrandDetailListView.as_view()),

    # 新增spu-获取所有一级分类
    url(r'^goods/channel/categories/$', spus_view.GoodCategoryListView.as_view()),

    # 新增spu-获取所有二,三级分类
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', spus_view.GoodCategoryListView.as_view()),

    # 新增规格选项-获取规格名称
    url(r'^goods/specs/simple/$', spec_opt_view.SpecListView.as_view()),

    # 新增sku图片-获取sku名称
    url(r'^skus/simple/$', image_view.SKUDetailListView.as_view()),

    # 新增频道-获取频道组
    url(r'^goods/channel_types/$', channel_views.GoodChannelModelListView.as_view()),

    # 新增频道-获取一级商品类别
    url(r'^goods/categories/$', channel_views.GoodCategoryListView.as_view()),

    # 商品订单状态修改
    url(r'^orders/(?P<pk>\d+)/status/$', orders_view.OrderModelViewSet.as_view(
        {'patch': 'partial_update'})),

    # 新增权限-获取权限类型
    url(r'^permission/content_types/$', perm_views.ContentTypeModelViewSet.as_view()),

    # 新增用户组-获取权限类型
    url(r'^permission/simple/$', group_views.PermSimpleListView.as_view()),

    # 新增管理员-获取用户分组
    url(r'^permission/groups/simple/$', admin_views.GroupSimpleListView.as_view()),

]

# 实例化router
router = SimpleRouter()
# 商品品牌管理
router.register(prefix=r'goods/brands', viewset=brand_views.BrandModelViewSet, base_name='brand')

# 商品频道管理
router.register(prefix=r'goods/channels', viewset=channel_views.ChannelModelViewSet, base_name='channel')

# 商品图片管理
router.register(prefix=r'skus/images', viewset=image_view.ImageModelViewSet, base_name='sku_image')

# 商品规格选项管理
router.register(prefix=r'specs/options', viewset=spec_opt_view.SpecOptModelViewSet, base_name='spec_opt')

# 商品规格管理
router.register(prefix=r'goods/specs', viewset=spec_view.SPUSpecModelViewSet, base_name='spu_spec')

# 商品spu管理
router.register(prefix=r'goods', viewset=spus_view.SPUDetailModelViewSet, base_name='spu_detail')

# 商品sku管理
router.register(prefix=r'skus', viewset=skus_view.SKUGoodsView, base_name='sku_detail')

# 商品订单管理
router.register(prefix=r'orders', viewset=orders_view.OrderModelViewSet, base_name='order')

# 权限管理
router.register(prefix=r'permission/perms', viewset=perm_views.PermModelViewSet, base_name='permission')

# 用户组管理
router.register(prefix=r'permission/groups', viewset=group_views.GroupModelViewSet, base_name='group')

# 管理员管理
router.register(prefix=r'permission/admins', viewset=admin_views.AdminModelViewSet, base_name='admin')

# 添加到路由列表
urlpatterns += router.urls



