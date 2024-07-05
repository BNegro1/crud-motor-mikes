# populate_db.py
import os
import django

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferremas.settings')
django.setup()

from usuarios.models import Product

products = [
    {"product_id": "001", "brand": "Desconocida", "name": "Martillo", "price": 10.00, "stock": 50, "category": "Herramientas"},
    {"product_id": "002", "brand": "Desconocida", "name": "Destornillador", "price": 5.00, "stock": 100, "category": "Herramientas"},
    {"product_id": "003", "brand": "Desconocida", "name": "Llave", "price": 8.00, "stock": 75, "category": "Herramientas"},
    {"product_id": "004", "brand": "Desconocida", "name": "Taladro", "price": 50.00, "stock": 30, "category": "Herramientas"},
    {"product_id": "005", "brand": "Desconocida", "name": "Sierra", "price": 25.00, "stock": 40, "category": "Herramientas"},
    {"product_id": "006", "brand": "Desconocida", "name": "Lijadora", "price": 35.00, "stock": 20, "category": "Herramientas"},
    {"product_id": "007", "brand": "Desconocida", "name": "Cemento", "price": 7.00, "stock": 150, "category": "Materiales de Construcción"},
    {"product_id": "008", "brand": "Desconocida", "name": "Arena", "price": 3.00, "stock": 200, "category": "Materiales de Construcción"},
    {"product_id": "009", "brand": "Desconocida", "name": "Ladrillo", "price": 0.50, "stock": 500, "category": "Materiales de Construcción"},
    {"product_id": "010", "brand": "Desconocida", "name": "Pintura", "price": 15.00, "stock": 60, "category": "Acabados"},
    {"product_id": "011", "brand": "Desconocida", "name": "Barniz", "price": 12.00, "stock": 45, "category": "Acabados"},
    {"product_id": "012", "brand": "Desconocida", "name": "Cerámico", "price": 20.00, "stock": 30, "category": "Acabados"},
    {"product_id": "013", "brand": "Desconocida", "name": "Casco", "price": 8.00, "stock": 100, "category": "Equipos de Seguridad"},
    {"product_id": "014", "brand": "Desconocida", "name": "Guantes", "price": 4.00, "stock": 120, "category": "Equipos de Seguridad"},
    {"product_id": "015", "brand": "Desconocida", "name": "Lentes de Seguridad", "price": 6.00, "stock": 80, "category": "Equipos de Seguridad"},
    {"product_id": "016", "brand": "Desconocida", "name": "Tornillo", "price": 0.10, "stock": 1000, "category": "Otros"},
    {"product_id": "017", "brand": "Desconocida", "name": "Anclaje", "price": 0.15, "stock": 800, "category": "Otros"},
    {"product_id": "018", "brand": "Desconocida", "name": "Adhesivo", "price": 5.00, "stock": 70, "category": "Otros"},
    {"product_id": "019", "brand": "Desconocida", "name": "Equipo de Medición", "price": 30.00, "stock": 25, "category": "Otros"},
]

for product_data in products:
    product, created = Product.objects.get_or_create(
        product_id=product_data["product_id"],
        defaults={
            "brand": product_data["brand"],
            "name": product_data["name"],
            "price": product_data["price"],
            "stock": product_data["stock"],
            "category": product_data["category"],
        }
    )
    if created:
        print(f'Producto {product.name} creado.')
    else:
        print(f'Producto {product.name} ya existe.')