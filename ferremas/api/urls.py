# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, webpay_return, webpay_final, view_cart, checkout

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('webpay/init/', checkout, name='webpay_init'),  # Directly map to checkout if it handles initiation
    path('webpay/return/', webpay_return, name='webpay_return'),
    path('webpay/final/', webpay_final, name='webpay_final'),
    path('cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
]
