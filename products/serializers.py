import imp
from pyexpat import model
from statistics import mode
from unicodedata import category
#imports from rest framework
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

#imports from models inside the app
from .models import Product, ProductDetailPhoto, Category, Tag

class CategorySerializer(ModelSerializer):
    thumbnail = serializers.CharField()
    class Meta:
        model = Category
        fields = ['id', 'title','image_alt','thumbnail']
    
    def create(self, validated_data):
        category = Category.from_validated_data(validated_data)

        if 'thumbnail' in validated_data:
            category.thumbnail = validated_data['thumbnail']
        category.save()
        return category
    
    def update(self, instance, validated_data):
        if "thumbnail" in validated_data:
            instance.thumbnail = validated_data['thumbnail']
        
        return super().update(instance, validated_data)
    
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class ProductSerializer(ModelSerializer):
    thumbnail = serializers.CharField()
    product_photos = serializers.SerializerMethodField()


    def get_product_photos(self, product):
        return ProductDetailPhoto.objects.filter(product=product).values_list('url', flat=True)
    class Meta:
        model = Product
        fields = ['id', 'title','price','thumbnail','is_trending','stock','description','product_photos']
    
    def create(self, validated_data):
        product = Product.from_validated_data(validated_data)

        if 'thumbnail' in validated_data:
            product.thumbnail = validated_data['thumbnail']
        product.save()
        return product
    
    def update(self, instance, validated_data):
        if "thumbnail" in validated_data:
            instance.thumbnail = validated_data['thumbnail']
        
        return super().update(instance, validated_data)
