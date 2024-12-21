from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        customer = request.user
        user_not_login = "none"  # Ẩn phần đăng nhập
        user_login = "block"  # Hiển thị phần đăng xuất
    else:
        user_not_login = "block"  # Hiển thị phần đăng nhập
        user_login = "none"  # Ẩn phần đăng xuất
    context = {'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'index.html', context)

def pages(request):
    return render(request,'pages.html')

def about(request):
    if request.user.is_authenticated:
        customer = request.user
        user_not_login = "none"  # Ẩn phần đăng nhập
        user_login = "block"  # Hiển thị phần đăng xuất
    else:
        user_not_login = "block"  # Hiển thị phần đăng nhập
        user_login = "none"  # Ẩn phần đăng xuất
    context = {'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'about-us.html',context)

def contact(request):
    if request.user.is_authenticated:
        customer = request.user
        user_not_login = "none"  # Ẩn phần đăng nhập
        user_login = "block"  # Hiển thị phần đăng xuất
    else:
        user_not_login = "block"  # Hiển thị phần đăng nhập
        user_login = "none"  # Ẩn phần đăng xuất
    context = {'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'contact.html',context)

def blog(request):
    if request.user.is_authenticated:
        customer = request.user
        user_not_login = "none"  # Ẩn phần đăng nhập
        user_login = "block"  # Hiển thị phần đăng xuất
    else:
        user_not_login = "block"  # Hiển thị phần đăng nhập
        user_login = "none"  # Ẩn phần đăng xuất
    context = {'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'blog.html',context)

def blogdetail(request):
    if request.user.is_authenticated:
        customer = request.user
        user_not_login = "none"  # Ẩn phần đăng nhập
        user_login = "block"  # Hiển thị phần đăng xuất
    else:
        user_not_login = "block"  # Hiển thị phần đăng nhập
        user_login = "none"  # Ẩn phần đăng xuất
    context = {'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'blog-details.html',context)

def booking(request):
    return render(request, 'booking.html')

def main(request):
    return render(request, 'main.html')

def rooms(request):
    if request.user.is_authenticated:
        customer = request.user
        user_not_login = "none"  # Ẩn phần đăng nhập
        user_login = "block"  # Hiển thị phần đăng xuất
    else:
        user_not_login = "block"  # Hiển thị phần đăng nhập
        user_login = "none"  
    rooms = Room.objects.all()
    context = {'rooms': rooms,'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'rooms.html',context)

def roomdetail(request):
    if request.user.is_authenticated:
        customer = request.user
        user_not_login = "none"  # Ẩn phần đăng nhập
        user_login = "block"  # Hiển thị phần đăng xuất
    else:
        user_not_login = "block"  # Hiển thị phần đăng nhập
        user_login = "none"  # Ẩn phần đăng xuất
    context = {'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'room-details.html',context)

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
        
    return render(request,'signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if  request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:messages.info(request, 'Username or password is incorrect')    
    
    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')
def promotion(request):
    if request.user.is_authenticated:
        customer = request.user
        user_not_login = "none"  # Ẩn phần đăng nhập
        user_login = "block"  # Hiển thị phần đăng xuất
    else:
        user_not_login = "block"  # Hiển thị phần đăng nhập
        user_login = "none"  # Ẩn phần đăng xuất
    promotion = Promotion.objects.all()
    context = {'promotion': promotion,'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'promotion.html', context)

