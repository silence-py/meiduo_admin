from django.utils import timezone
import pytz
from django.conf import settings


def get_cur_0_time():
    cur_time = timezone.now()  # 获取当前时间, 默认时区为"UTC"
    # 获取当日零时
    cur_time = cur_time.astimezone(tz=pytz.timezone(settings.TIME_ZONE))
    local_0_time = cur_time.replace(hour=0, minute=0, second=0)
    return local_0_time
