from django.urls import path
from .views import contact, login_view, logout_view, register_view, index_view, cliente_dashboard, add_to_cart, view_cart, checkout
urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('cliente/', cliente_dashboard, name='cliente_dashboard'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
]
