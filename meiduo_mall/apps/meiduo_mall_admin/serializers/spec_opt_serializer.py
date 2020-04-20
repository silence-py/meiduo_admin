from rest_framework import serializers
from goods.models import SpecificationOption, SPUSpecification


class SPUSpecModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPUSpecification
        fields = ['id', 'name']


class SpecOptModelSerializer(serializers.ModelSerializer):
    """spu规格和选项序列化模型"""
    spec = serializers.StringRelatedField()
    spec_id = serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = '__all__'
