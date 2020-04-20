from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.conf import settings
from datetime import datetime
from datetime import timedelta
from rest_framework.generics import ListAPIView
import pytz
from meiduo_mall_admin.utils.get_cur_0_time import get_cur_0_time

from users.models import User


class UserTotalView(APIView):

    """查询用户总量"""
    def get(self, request):
        # 查询用户总量
        count = User.objects.count()

        cur_time = datetime.now()
        # 构建响应
        return Response(data={
            'count': count,
            'date': cur_time.date()
        })


class DayIncreaseUserView(APIView):
    """查询当日新增用户"""
    def get(self, request):

        # # cur_time = datetime.today()
        # cur_time = timezone.now()   # 获取当前时间, 默认时区为"UTC"
        # # 获取当日零时
        # cur_time = cur_time.astimezone(tz=pytz.timezone(settings.TIME_ZONE))
        # local_0_time = cur_time.replace(hour=0, minute=0, second=0)
        local_0_time = get_cur_0_time()

        # 查询当日新增用户数量
        count = User.objects.filter(date_joined__gte=local_0_time).count()

        return Response(data={
            'count': count,
            'date': local_0_time.date()
        })


class DayActiveUserView(APIView):
    """查询当日活跃用户"""
    def get(self, request):
        local_0_time = get_cur_0_time()

        # 查询当日活跃用户数量
        count = User.objects.filter(last_login__gte=local_0_time).count()

        return Response(data={
            'count': count,
            'date': local_0_time.date()
        })


class DayOrderView(APIView):
    """查询当日下单数量"""
    def get(self, request):

        local_0_time = get_cur_0_time()

        # 查询当日下单所有用户
        users = User.objects.filter(orders__create_time__gte=local_0_time)

        # 对用户进行去重过滤
        count = len(set(users))

        return Response(data={
            'count': count,
            'date': local_0_time.date()
        })


class MonthIncreaseUserView(APIView):
    """近30天新增用户数量统计"""
    def get(self, request):
        # 获取当日零时
        end_0_time = get_cur_0_time()
        # 获取起始日零时
        start_0_time = end_0_time-timedelta(days=29)

        res = []

        for index in range(30):
            # 获取计算日0时
            cur_0_time = start_0_time + timedelta(days=index)
            # 获取计算日下日0时
            next_0_time = cur_0_time + timedelta(days=1)
            # 获取计算日新增用户数量
            count = User.objects.filter(date_joined__gte=cur_0_time,
                                        date_joined__lt=next_0_time).count()
            # 追加列表, 构建响应数据
            res.append(
                {
                    'count': count,
                    'date': cur_0_time.date()
                }
            )
        return Response(data=res)


from goods.models import GoodsVisitCount
from meiduo_mall_admin.serializers.index_serializer import *


class DayGoodVisitView(ListAPIView):
    queryset = GoodsVisitCount.objects.all()
    serializer_class = DayGoodVisitModelSerializer

    def get_queryset(self):
        cur_0_time = get_cur_0_time()
        return self.queryset.filter(create_time__gte=cur_0_time)

