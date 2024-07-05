from django.urls import path
from .views import login_view, logout_view, register_view, index_view, tienda_view, add_to_cart, view_cart, checkout

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('tienda/', tienda_view, name='tienda'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
]
