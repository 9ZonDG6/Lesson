from django.urls import path, include
from shop import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('product/<slug:product_slug>', views.ProductView.as_view(), name='product'),
    path('redirect/', views.Redirect.as_view(), name='redirect'),
    path('drf/', views.ProductAPI.as_view(), name='product_api'),
] + router.urls
