from django.urls import path
from .views import admin_dashboard, vendedor_dashboard, approve_order, reject_order, bodeguero_dashboard, accept_order, contador_dashboard, confirm_payment, register_delivery

urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),
    path('vendedor/', vendedor_dashboard, name='vendedor_dashboard'),
    path('approve_order/<int:order_id>/', approve_order, name='approve_order'),
    path('reject_order/<int:order_id>/', reject_order, name='reject_order'),
    path('bodeguero/', bodeguero_dashboard, name='bodeguero_dashboard'),
    path('accept_order/<int:order_id>/', accept_order, name='accept_order'),
    path('contador/', contador_dashboard, name='contador_dashboard'),
    path('confirm_payment/<int:payment_id>/', confirm_payment, name='confirm_payment'),
    path('register_delivery/<int:delivery_id>/', register_delivery, name='register_delivery'),
]
