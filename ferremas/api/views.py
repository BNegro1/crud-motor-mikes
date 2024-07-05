from rest_framework import viewsets
from admin_dashboard.models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from django.shortcuts import render, redirect
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.webpay.webpay_plus.transaction import WebpayOptions
from transbank.common.integration_type import IntegrationType
import random
from django.conf import settings

def webpay_init(request):
    buy_order = str(random.randint(100000, 999999))
    session_id = request.session.session_key
    amount = request.GET.get('amount')
    return_url = settings.WEBPAY_RETURN_URL

    tx = Transaction(WebpayOptions(
        commerce_code=settings.WEBPAY_COMMERCE_CODE,
        api_key=settings.WEBPAY_API_KEY,
        integration_type=IntegrationType.TEST  # Cambiar a .LIVE en producción
    ))
    response = tx.create(buy_order, session_id, amount, return_url)
    return redirect(response['url'] + '?token_ws=' + response['token'])

def webpay_return(request):
    token = request.GET.get('token_ws')
    tx = Transaction(WebpayOptions(
        commerce_code=settings.WEBPAY_COMMERCE_CODE,
        api_key=settings.WEBPAY_API_KEY,
        integration_type=IntegrationType.TEST  # Cambiar a .LIVE en producción
    ))
    response = tx.commit(token)
    if response['status'] == 'AUTHORIZED':
        return redirect(settings.WEBPAY_FINAL_URL + '?token_ws=' + token)
    else:
        return render(request, 'webpay/error.html')

def webpay_final(request):
    token = request.GET.get('token_ws')
    tx = Transaction(WebpayOptions(
        commerce_code=settings.WEBPAY_COMMERCE_CODE,
        api_key=settings.WEBPAY_API_KEY,
        integration_type=IntegrationType.TEST  # Cambiar a .LIVE en producción
    ))
    response = tx.status(token)
    if response['status'] == 'AUTHORIZED':
        return render(request, 'webpay/success.html', {'response': response})
    else:
        return render(request, 'webpay/error.html')
