# delete_products.py
import os
import django

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferremas.settings')
django.setup()

from admin_dashboard.models import Product

def delete_all_products():
    # Obtiene el número total de productos antes de la eliminación
    total_products = Product.objects.count()
    
    # Elimina todos los productos
    Product.objects.all().delete()
    
    # Verifica cuántos productos quedan después de la eliminación
    remaining_products = Product.objects.count()
    
    print(f"Se han eliminado {total_products} productos.")
    print(f"Productos restantes: {remaining_products}")

if __name__ == "__main__":
    # Pide confirmación antes de proceder
    confirm = input("¿Estás seguro de que quieres eliminar todos los productos? (s/n): ")
    if confirm.lower() == 's':
        delete_all_products()
    else:
        print("Operación cancelada.")