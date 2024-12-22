from django.shortcuts import get_object_or_404, render, redirect

from app.form import PromotionForm, RoomForm
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
    if request.user.is_authenticated:
        customer = request.user
        user_not_login = "none"  # Ẩn phần đăng nhập
        user_login = "block"  # Hiển thị phần đăng xuất
    else:
        user_not_login = "block"  # Hiển thị phần đăng nhập
        user_login = "none"  # Ẩn phần đăng xuất

    # Fetch the room id from the 'roomdetail' page or from URL parameters
    id = request.GET.get('id', '')
    if id:
        rooms = Room.objects.filter(id=id)
    else:
        rooms = Room.objects.none()  # Or handle the case where 'id' is not provided

    context = {'rooms': rooms, 'user_not_login': user_not_login, 'user_login': user_login}
    return render(request, 'booking.html', context)


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
    id = request.GET.get('id','')
    rooms = Room.objects.filter(id=id)
    context = {'rooms':rooms,'user_not_login': user_not_login, 'user_login': user_login}
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
    return render(request, 'promotion.html',context)

def manage_promotions(request):
    promotions = Promotion.objects.all()  
    context = {'promotions': promotions}
    return render(request, 'promotion-management.html', context)

def add_promotion(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the promotion to the database
            return redirect('manage_promotions')  # Redirect after saving
    else:
        form = PromotionForm()  # Create an empty form instance

    return render(request, 'promotion-management.html/#addPromotionModal', {'form': form})
# Edit promotion (Update an existing promotion)
def edit_promotion(request, id):
    promotion = get_object_or_404(Promotion, id=id)  # Fetch the promotion to edit
    if request.method == 'POST':
        form = PromotionForm(request.POST, request.FILES, instance=promotion)
        if form.is_valid():
            form.save()
            return redirect('manage_promotions')  # Redirect to the manage promotions page after saving
    else:
        form = PromotionForm(instance=promotion)
    return render(request, 'promotion-management.html/#editPromotionModal', {'form': form, 'promotion': promotion})

# Delete promotion (Remove a promotion)
def delete_promotion(request, id):
    promotion = get_object_or_404(Promotion, id=id)  # Fetch the promotion to delete
    promotion.delete()
    return redirect('manage_promotions') 

def manage_room(request):
    rooms = Room.objects.all()  
    context = {'rooms': rooms}
    return render(request, 'quanliphong.html', context)
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the promotion to the database
            return redirect('manage_room')  # Redirect after saving
    else:
        form = RoomForm()  # Create an empty form instance

    return render(request, 'room-management.html', {'form': form})
def delete_room(request, id):
    room = get_object_or_404(Room, id=id)  # Fetch the promotion to delete
    room.delete()
    return redirect('manage_room') 
def edit_room(request, id):
    room = get_object_or_404(Room, id=id)  # Fetch the promotion to edit
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('manage_room')  # Redirect to the manage promotions page after saving
    else:
        form = RoomForm(instance=room)
    return render(request, 'quanliphong.html/#editRoomModal', {'form': form, 'rooms': rooms})
def check_in_view(request):
    rooms = Room.objects.all()  # Lấy danh sách phòng từ database
    return render(request, 'checkin.html', {'rooms': rooms})
def check_out_view(request):
    rooms = Room.objects.all()
    
    return render(request, 'checkout.html', {'rooms': rooms})
def thongkedoanhthu(request):
    # Dữ liệu giả lập
    revenue_data = {
        "totalRevenue": 50000000,
        "roomRevenue": 30000000,
        "serviceRevenue": 10000000,
        "promotionRevenue": 10000000,
        "dailyRevenue": [1000000, 1500000, 1200000, 1800000, 2200000],
        "dailyLabels": ['01/12', '02/12', '03/12', '04/12', '05/12'],
        "serviceRevenueData": [5000000, 15000000, 10000000],
        "serviceLabels": ['Phòng', 'Dịch vụ', 'Khuyến mãi'],
    }
    context = {
        "total_revenue": revenue_data["totalRevenue"],
        "room_revenue": revenue_data["roomRevenue"],
        "service_revenue": revenue_data["serviceRevenue"],
        "promotion_revenue": revenue_data["promotionRevenue"],
        "revenue_data": revenue_data,
    }
    return render(request, 'thongkedoanhthu.html', context)