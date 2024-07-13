from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CustomUser, Client, Product, Order, Payment, Delivery

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        role = request.POST['role']
        user = CustomUser.objects.create_user(username=username, password=password, email=email, role=role)
        if role == 'Cliente':
            Client.objects.create(user=user)
        login(request, user)
        return redirect('index')
    return render(request, 'register.html')

def index_view(request):
    return render(request, 'inicioGeneral.html')


def tienda_view(request):
    tools = Product.objects.filter(category='Herramientas')
    materials = Product.objects.filter(category='Materiales de Construcción')
    finishes = Product.objects.filter(category='Acabados')
    safety = Product.objects.filter(category='Equipos de Seguridad')
    others = Product.objects.filter(category='Otros')
    
    return render(request, 'tienda.html', {
        'tools': tools,
        'materials': materials,
        'finishes': finishes,
        'safety': safety,
        'others': others,
    })

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        if product.stock > 0:
            order, created = Order.objects.get_or_create(product=product, client_name=request.user.username, status='Pending', defaults={'quantity': 1})
            if not created:
                order.quantity += 1
                order.save()
            product.stock -= 1
            product.save()
            return JsonResponse({'success': True, 'stock': product.stock, 'quantity': order.quantity})
        else:
            return JsonResponse({'success': False, 'error': 'Producto agotado'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)

@login_required
def view_cart(request):
    orders = Order.objects.filter(client_name=request.user.username, status='Pending')
    return render(request, 'view_cart.html', {'orders': orders})

@login_required
def checkout(request):
    if request.method == 'POST':
        orders = Order.objects.filter(client_name=request.user.username, status='Pending')
        total_amount = sum(order.product.price * order.quantity for order in orders)
        for order in orders:
            order.status = 'Approved'
            order.save()
            Payment.objects.create(order=order, amount=order.product.price * order.quantity, status='Pending')
        return redirect('tienda')
    return render(request, 'checkout.html')


