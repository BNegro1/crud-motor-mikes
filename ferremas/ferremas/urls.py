from django.contrib import admin
from django.urls import path, include
from usuarios.views import index_view
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='inicioGeneral'),  # URL raíz que apunta a la vista `index_view`
    path('api/', include('api.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('admin_dashboard/', include('admin_dashboard.urls')),
]