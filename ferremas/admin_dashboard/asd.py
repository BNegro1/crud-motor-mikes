from admin_dashboard.models import Product, Order

# Verificar productos
products = Product.objects.all()
for product in products:
    print(product.name, product.price, product.stock)

# Verificar pedidos
orders = Order.objects.all()
for order in orders:
    print(order.product.name, order.quantity, order.status, order.client_name)
