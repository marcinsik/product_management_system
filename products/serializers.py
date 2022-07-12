from rest_framework import serializers
from products.models import Product,Warehouse


class WarehouseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = ('id', 'name', 'address')

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'created_at', 'warehouse')

class ProductDetailSerializer(serializers.ModelSerializer):

    warehouse = WarehouseListSerializer(required=True)


    class Meta:
        model = Product
        fields = '__all__'

class AddProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class AddWarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = ('id', 'name', 'created_at', 'warehouse')
