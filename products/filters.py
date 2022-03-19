from django_filters import rest_framework as filters, NumberFilter

from .models import Product


class ProductFilter(filters.FilterSet):
    price__gte = NumberFilter(field_name="price", lookup_expr="gte")
    price__lte = NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["price__gte", "price__lte", "is_trending", "category__title", "is_deleted"]