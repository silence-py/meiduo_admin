from django.core.files.storage import Storage
from django.conf import settings
from django.utils import timezone
from fdfs_client.client import Fdfs_client
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class FdfsStorage(Storage):
    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content, max_length=None):
        """name: 文件名, content: file文件对象"""
        pass
        # # 实例化对象
        # f_cli = Fdfs_client(settings.FDFS_PATH)
        #
        # # 上传图片
        # res = f_cli.upload_by_buffer(content.read())
        #
        # # 校验图片是否上传成功
        # if res['Status'] != 'Upload successed.':
        #     raise ValidationError('图片上传失败')
        #
        # # 校验成功返回唯一标识
        # return res['Remote file_id']


    # def exists(self, name):
    #     # 返回False: 不管图片是否存在仍然上传
    #     return False

    def url(self, name):
        return settings.FDFS_URL + name
