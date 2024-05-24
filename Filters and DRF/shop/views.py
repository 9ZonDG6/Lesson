from django.views.generic import ListView, RedirectView

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category
from shop import filters
from .serializers import ProductSerializer


class IndexView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/index.html'

    def get_filters(self):
        return filters.ProductFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['filters'] = self.get_filters()
        context['title'] = 'Список товаров'
        return context


class ProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/product.html'

    def get_filters(self):
        return filters.ProductFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        product = Product.objects.get(slug=self.kwargs['product_slug'])
        context['filters'] = self.get_filters()
        context['title'] = product.title
        context['product'] = product
        context['selected_category'] = product.category
        return context


class ProductAPI(APIView):
    def get(self, request):
        qs = Product.objects.all()
        title = [p.title for p in qs]

        return Response(title)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filterset_class = filters.Product
    serializer_class = ProductSerializer


class Redirect(RedirectView):
    query_string = True
    url = 'https://github.com/9ZonDG6/gjango-project'
