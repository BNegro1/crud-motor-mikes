from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.general_dashboard, name='general_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('bodeguero/', views.bodeguero_dashboard, name='bodeguero_dashboard'),
    path('contador/', views.contador_dashboard, name='contador_dashboard'),
    path('vendedor/', views.vendedor_dashboard, name='vendedor_dashboard'),
    path('accept_order/<int:order_id>/', views.accept_order, name='accept_order'),
    path('approve_order/<int:order_id>/', views.approve_order, name='approve_order'),
    path('reject_order/<int:order_id>/', views.reject_order, name='reject_order'),
    path('confirm_payment/<int:payment_id>/', views.confirm_payment, name='confirm_payment'),
    path('register_delivery/<int:delivery_id>/', views.register_delivery, name='register_delivery'),
]
