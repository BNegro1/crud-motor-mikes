from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=[
        ('Cliente', 'Cliente'),
        ('Administrador', 'Administrador'),
        ('Vendedor', 'Vendedor'),
        ('Bodeguero', 'Bodeguero'),
        ('Contador', 'Contador'),
    ])
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='customuser',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='customuser',
    )
