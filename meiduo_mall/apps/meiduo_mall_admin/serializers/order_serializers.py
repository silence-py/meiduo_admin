
from rest_framework import serializers
from orders.models import OrderInfo, OrderGoods
from goods.models import SKU


class OrderModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderInfo
        fields = [
            'order_id',
            'create_time'
        ]


class OrderSKUModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ['name', 'default_image']


class OrderGoodModelSerializer(serializers.ModelSerializer):

    sku = OrderSKUModelSerializer()

    class Meta:
        model = OrderGoods
        fields = ['count', 'price', 'sku']


class OrderDetailModelSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    skus = OrderGoodModelSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'