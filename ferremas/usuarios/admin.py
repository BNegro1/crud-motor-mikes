from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Importar UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'rut')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Client)
admin.site.register(SalesReport)
admin.site.register(PerformanceReport)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Delivery)
