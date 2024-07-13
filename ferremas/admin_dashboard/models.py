from django.db import models

class SalesReport(models.Model):
    month = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    store_performance = models.TextField()

class PerformanceReport(models.Model):
    store_name = models.CharField(max_length=100)
    performance = models.TextField()
    report_date = models.DateField()

class Product(models.Model):
    product_id = models.CharField(max_length=20)
    brand = models.CharField(max_length=50, default='Desconocida')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=50, default='Categoría desconocida')  

    def __str__(self):
        return self.name
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Pending')
    client_name = models.CharField(max_length=100)
    client_address = models.CharField(max_length=200)
    client_email = models.EmailField()

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')], default='Pending')
    payment_date = models.DateField()

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending')
    delivery_date = models.DateField(null=True, blank=True)
