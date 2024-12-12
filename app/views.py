from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Trang chủ
def home(request):
    return render(request, 'index.html')

# Trang giới thiệu
def about(request):
    return render(request, 'about.html')

# Trang liên hệ
def contact(request):
    return render(request, 'contact.html')

# Trang sự kiện
def events(request):
    return render(request, 'events.html')

# Đăng nhập người dùng
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Tên tài khoản hoặc mật khẩu không đúng!')
            return render(request, 'login.html', {'invalid': 'Tên tài khoản hoặc mật khẩu không đúng!'})
    return render(request, 'login.html')

# Trang phòng
def rooms(request):
    return render(request, 'rooms.html')

# Đăng ký người dùng
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Mật khẩu không khớp!')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Tên tài khoản đã tồn tại!')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email đã được sử dụng!')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Đăng ký thành công!')
        return redirect('login')
    return render(request, 'signup.html')