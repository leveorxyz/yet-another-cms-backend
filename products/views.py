from django.shortcuts import render
from core.views import CustomListAPIView,CustomRetrieveUpdateDestroyAPIView,CustomCreateAPIView
from .models import Category, Tag, Product
from .serializers import CategorySerializer, TagSerializer, ProductSerializer
from rest_framework.generics import CreateUpdateRetrieveDestroyAPIView

# Create your views here.

class CategoryListView(CustomListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateView(CustomCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(CustomRetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(CustomListAPIView):
    serializer_class = ProductSerializer
    