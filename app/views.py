from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pages(request):
    return render(request,'pages.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blogdetail(request):
    return render(request, 'blog-details.html')

def booking(request):
    return render(request, 'booking.html')

def main(request):
    return render(request, 'main.html')

def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'rooms.html',context)

def roomdetail(request):
    return render(request, 'room-details.html')

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tài khoản mới đã được tạo: {username}')
            login(request, user)
            return redirect('login')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')
        
    return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')
    else:
        form = AuthenticationForm
        return render(request, 'login.html', {'form':form})

def logout(request):
    logout(request)
    return redirect('login')
def promotion(request):
    promotion = Promotion.objects.all()
    context = {'promotion': promotion}
    return render(request, 'promotion.html', context)

