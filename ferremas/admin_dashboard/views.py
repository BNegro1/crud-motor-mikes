from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import SalesReport, PerformanceReport, Product, Order, Payment, Delivery

def admin_dashboard(request):
    sales_reports = SalesReport.objects.all()
    performance_reports = PerformanceReport.objects.all()
    return render(request, 'admin_dashboard.html', {
        'sales_reports': sales_reports,
        'performance_reports': performance_reports
    })

def vendedor_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.filter(status='Pending')
    return render(request, 'vendedor_dashboard.html', {
        'products': products,
        'orders': orders
    })

def approve_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Approved'
    order.save()
    return HttpResponseRedirect(reverse('vendedor_dashboard'))

def reject_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Rejected'
    order.save()
    return HttpResponseRedirect(reverse('vendedor_dashboard'))

def bodeguero_dashboard(request):
    orders = Order.objects.filter(status='Approved')
    return render(request, 'bodeguero_dashboard.html', {
        'orders': orders
    })

def accept_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    Delivery.objects.create(order=order, status='Pending')
    return HttpResponseRedirect(reverse('bodeguero_dashboard'))

def contador_dashboard(request):
    payments = Payment.objects.filter(status='Pending')
    deliveries = Delivery.objects.filter(status='Pending')
    return render(request, 'contador_dashboard.html', {
        'payments': payments,
        'deliveries': deliveries
    })

def confirm_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.status = 'Confirmed'
    payment.save()
    return HttpResponseRedirect(reverse('contador_dashboard'))

def register_delivery(request, delivery_id):
    delivery = get_object_or_404(Delivery, id=delivery_id)
    delivery.status = 'Delivered'
    delivery.delivery_date = datetime.now()
    delivery.save()
    return HttpResponseRedirect(reverse('contador_dashboard'))
