from django.contrib import admin
from .models import SalesReport, PerformanceReport, Product, Order, Payment, Delivery

admin.site.register(SalesReport)
admin.site.register(PerformanceReport)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Delivery)
