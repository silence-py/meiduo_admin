# from users.models import User
# from django.utils import timezone
# from django.conf import settings
# import pytz


def custom_jwt_response(token, user=None, request=None):
    # try:
    #     user = User.objects.get(username=user.username)
    # except User.DoesNotExist:
    #     return None
    # cur_time = timezone.now()
    # user.last_login = cur_time.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))
    # user.save()
    return {
        'username': user.username,
        'user_id': user.id,
        'token': token
    }