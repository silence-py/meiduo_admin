from rest_framework.response import Response
from rest_framework import serializers
from users.models import User


class UserListCreateModelSerializer(serializers.ModelSerializer):
    """用户信息序列化模型"""
    class Meta:
        # 指定模型类
        model = User
        # 指定字段
        fields = [
            'id',
            'username',
            'mobile',
            'email',
            'password'
        ]
        # 添加字段约束
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8, 'max_length': 20},
            'username': {'min_length': 2, 'max_length': 20}
        }

    # 重写create方法
    def create(self, validated_data):
        # 创建超级管理员用户(自动实现密码加密)
        instance = User.objects.create_superuser(**validated_data)
        return instance

