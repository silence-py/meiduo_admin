from rest_framework import serializers
from goods.models import SKU, SKUSpecification, GoodsCategory, SPU, SPUSpecification, SpecificationOption


class SKUSpecOptModelSerializer(serializers.ModelSerializer):
    """商品sku规格序列化模型"""
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification
        fields = ['spec_id', 'option_id']


class SKUGoodModelSerializer(serializers.ModelSerializer):
    """商品sku序列化模型"""
    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    specs = SKUSpecOptModelSerializer(many=True)

    class Meta:
        model = SKU
        fields = "__all__"

    def create(self, validated_data):
        # specs 将规格选项单独取出
        specs = validated_data.pop('specs')
        # 新建sku模型对象
        sku = super().create(validated_data)
        for spec in specs:
            spec['sku_id'] = sku.id
            SKUSpecification.objects.create(**spec)
        return sku

    def update(self, instance, validated_data):
        # 将规格选项单独取出
        specs = validated_data.pop('specs')
        # 更新数据
        sku = super().update(instance, validated_data)

        # 删除之前的规格选项,替换新增的规格选项
        SKUSpecification.objects.filter(sku_id=sku.id).delete()

        for spec in specs:
            spec['sku_id'] = sku.id
            SKUSpecification.objects.create(**spec)
        return sku


class GoodCategoryModelSerializer(serializers.ModelSerializer):
    """商品类别序列化模型"""
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']


class SPUNameModelSerializer(serializers.ModelSerializer):
    """spu名称序列化模型"""
    class Meta:
        model = SPU
        fields = ['id', 'name']


class SpecOptModelSerializer(serializers.ModelSerializer):

    """spu规格和选项序列化模型"""
    class Meta:
        model = SpecificationOption
        fields = ['id', 'value']


class SPUSpecModelSerializer(serializers.ModelSerializer):
    """spu规格序列化模型"""
    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()

    # 外键关联序列化字段
    options = SpecOptModelSerializer(many=True)

    class Meta:
        model = SPUSpecification
        fields = ["id", "name", "spu", "spu_id", "options"]