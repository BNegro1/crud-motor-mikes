from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import SalesReport, PerformanceReport, Product, Order, Payment, Delivery

def admin_dashboard(request):
    sales_reports = SalesReport.objects.all()
    performance_reports = PerformanceReport.objects.all()
    return render(request, 'admin_dashboard/admin_dashboard.html', {
        'sales_reports': sales_reports,
        'performance_reports': performance_reports
    })

def bodeguero_dashboard(request):
    orders = Order.objects.filter(status='Approved')
    return render(request, 'admin_dashboard/bodeguero_dashboard.html', {
        'orders': orders
    })

def contador_dashboard(request):
    payments = Payment.objects.filter(status='Pending')
    deliveries = Delivery.objects.filter(status='Pending')
    return render(request, 'admin_dashboard/contador_dashboard.html', {
        'payments': payments,
        'deliveries': deliveries
    })

def vendedor_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.filter(status='Pending')
    return render(request, 'admin_dashboard/vendedor_dashboard.html', {
        'products': products,
        'orders': orders
    })

def accept_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Accepted'
    order.save()
    return redirect('bodeguero_dashboard')

def approve_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Approved'
    order.save()
    return redirect('vendedor_dashboard')

def reject_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Rejected'
    order.save()
    return redirect('vendedor_dashboard')

def confirm_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.status = 'Confirmed'
    payment.save()
    return redirect('contador_dashboard')

def register_delivery(request, delivery_id):
    delivery = get_object_or_404(Delivery, id=delivery_id)
    delivery.status = 'Delivered'
    delivery.delivery_date = timezone.now()
    delivery.save()
    return redirect('contador_dashboard')
