from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from core.views import CustomListAPIView,CustomRetrieveUpdateDestroyAPIView,CustomCreateAPIView
from .models import Category, Tag, Product
from .serializers import CategorySerializer, TagSerializer, ProductSerializer

# Create your views here.

class CategoryListView(CustomListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateView(CustomCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryEditView(CustomRetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(CustomListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = [ProductFilter]
    permission_classes = [
        AllowAny,
    ]
    search_fields = ["title"]

    def get_queryset(self):
        base_query = Product.objects.filter(stock__gt=0)

        return base_query