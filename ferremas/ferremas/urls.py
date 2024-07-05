from django.contrib import admin
from django.urls import path, include
from usuarios.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),  # URL raíz que apunta a la vista `index_view`
    path('usuarios/', include('usuarios.urls')),
    path('admin_dashboard/', include('admin_dashboard.urls')),
    path('api/', include('api.urls')),
]
