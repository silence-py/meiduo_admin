from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from fdfs_client.client import Fdfs_client

from goods.models import Brand


class BrandModelSerializer(serializers.ModelSerializer):
    """商品品牌"""
    class Meta:
        model = Brand
        fields = '__all__'

    def validate(self, attrs):

        # 实例化fdfs客户端对象(FDFS_PATH = 'meiduo_mall/client.conf')
        f_cli = Fdfs_client(settings.FDFS_PATH)
        
        # 获取图片对象
        logo = attrs['logo']

        # 上传图片
        res = f_cli.upload_by_buffer(logo.read())

        # 上传失败, 提前响应
        if res['Status'] != 'Upload successed.':
            raise ValidationError('图片上传失败')

        # 上传成功,替换原始数据
        attrs['logo'] = res['Remote file_id']

        # 返回数据
        return attrs 

    """
    def create(self, validated_data):

        # 实例化fdfs客户端对象(FDFS_PATH = 'meiduo_mall/client.conf')
        f_cli = Fdfs_client(settings.FDFS_PATH)

        # 获取图片对象
        logo = validated_data['logo']

        # 上传图片
        res = f_cli.upload_by_buffer(logo.read())

        # 上传失败, 提前响应
        if res['Status'] != 'Upload successed.':
            raise ValidationError('图片上传失败')

        # 上传成功,替换原始数据
        validated_data['logo'] = res['Remote file_id']

        # 新建模型对象
        instance = self.Meta.model.objects.create(**validated_data)

        # 返回数据
        return instance

    def update(self, instance, validated_data):

        # 实例化fdfs客户端对象(FDFS_PATH = 'meiduo_mall/client.conf')
        f_cli = Fdfs_client(settings.FDFS_PATH)

        # 获取图片对象
        logo = validated_data['logo']

        # 上传图片
        res = f_cli.upload_by_buffer(logo.read())

        # 上传失败, 提前响应
        if res['Status'] != 'Upload successed.':
            raise ValidationError('图片上传失败')

        # 上传成功,替换原始数据
        validated_data['logo'] = res['Remote file_id']

        # 新建模型对象
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        # 返回数据
        return instance
    """