
from rest_framework import serializers
from goods.models import GoodsChannel, GoodsChannelGroup


class ChannelGroupModelSerializer(serializers.ModelSerializer):
    """商品频道组"""
    class Meta:
        model = GoodsChannelGroup
        fields = '__all__'


class ChannelModelSerializer(serializers.ModelSerializer):
    """商品频道"""
    group = serializers.StringRelatedField()
    group_id = serializers.IntegerField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = GoodsChannel
        fields = '__all__'
