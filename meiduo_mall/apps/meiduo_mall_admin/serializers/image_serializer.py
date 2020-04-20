from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from fdfs_client.client import Fdfs_client
from django.conf import settings

from goods.models import SKUImage, SKU


class SKUDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['id', 'name']


class ImageModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKUImage
        fields = '__all__'

    # def validate(self, attrs):
    #
    #     # 实例化fdfs对象
    #     f_cli = Fdfs_client(settings.FDFS_PATH)
    #
    #     # 获取图片文件
    #     img = attrs.get('image')
    #
    #     # 上传图片到fdfs
    #     res = f_cli.upload_by_buffer(img.read())
    #
    #     # 校验是否上传成功 Upload successed.
    #     if res['Status'] != 'Upload successed.':
    #         raise ValidationError('图片上传失败')
    #
    #     # 上传成功接收返回值(图片唯一标识)
    #     img_url = res['Remote file_id']
    #
    #     # 替换原有数据并返回
    #     attrs['image'] = img_url
    #     return attrs

