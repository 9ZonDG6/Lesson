import django_filters
from shop.models import Product


class ProductFilter(django_filters.FilterSet):
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Цена от')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')

    class Meta:
        model = Product
        fields = ('category', 'in_stock')
