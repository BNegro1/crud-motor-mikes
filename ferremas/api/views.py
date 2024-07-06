# api/views.py
from rest_framework import viewsets
from usuarios.models import Product, Order, Payment
from .serializers import ProductSerializer
from django.shortcuts import render, redirect
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.webpay.webpay_plus.transaction import WebpayOptions
from transbank.common.integration_type import IntegrationType
import random
from django.conf import settings
from django.utils import timezone

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def view_cart(request):
    orders = Order.objects.filter(status='Pending')  
    return render(request, 'view_cart.html', {'orders': orders})


def checkout(request):
    if request.method == 'POST':

        orders = Order.objects.filter(status='Pending')
        total_amount = sum(order.product.price * order.quantity for order in orders)

        buy_order = str(random.randint(100000, 999999))
        session_id = request.session.session_key
        return_url = settings.WEBPAY_RETURN_URL

        tx = Transaction(WebpayOptions(
            commerce_code=settings.WEBPAY_COMMERCE_CODE,
            api_key=settings.WEBPAY_API_KEY,
            integration_type=IntegrationType.TEST 
        ))
        response = tx.create(buy_order, session_id, total_amount, return_url)
        
        for order in orders:
            Payment.objects.create(
                order=order,
                amount=order.product.price * order.quantity,
                status='Pending',
                payment_date=timezone.now()
            )

        return redirect(response['url'] + '?token_ws=' + response['token'])
    else:
        return render(request, 'checkout.html')

def webpay_init(request):
    # This function may not be necessary anymore if checkout handles payment initiation
    pass

def webpay_return(request):
    token = request.GET.get('token_ws')
    tx = Transaction(WebpayOptions(
        commerce_code=settings.WEBPAY_COMMERCE_CODE,
        api_key=settings.WEBPAY_API_KEY,
        integration_type=IntegrationType.TEST  
    ))
    response = tx.commit(token)
    if response['status'] == 'AUTHORIZED':

        orders = Order.objects.filter(status='Pending')
        for order in orders:
            order.status = 'Approved'
            order.save()
        return redirect(settings.WEBPAY_FINAL_URL + '?token_ws=' + token)
    else:
        return render(request, 'webpay/error.html')

def webpay_final(request):
    token = request.GET.get('token_ws')
    tx = Transaction(WebpayOptions(
        commerce_code=settings.WEBPAY_COMMERCE_CODE,
        api_key=settings.WEBPAY_API_KEY,
        integration_type=IntegrationType.TEST  
    ))
    response = tx.status(token)
    if response['status'] == 'AUTHORIZED':
        return render(request, 'webpay/success.html', {'response': response})
    else:
        return render(request, 'webpay/error.html')
