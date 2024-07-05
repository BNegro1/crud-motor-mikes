from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
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
        login(request, user)
        return redirect('dashboard')
    return render(request, 'register.html')
from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')
