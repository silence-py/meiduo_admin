

from rest_framework import serializers

from goods.models import SPU, Brand


class SPUDetailModelSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        fields = '__all__'
        extra_kwargs = {
            'category1': {'read_only': True},
            'category2': {'read_only': True},
            'category3': {'read_only': True}
        }


class BrandDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']
