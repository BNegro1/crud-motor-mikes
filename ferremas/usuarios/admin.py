from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Importar UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'rut')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
