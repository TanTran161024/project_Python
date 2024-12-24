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
        user_not_login = "none"  # Hide login section
        user_login = "block"  # Show logout section
    else:
        user_not_login = "block"  # Show login section
        user_login = "none"  # Hide logout section

    # Get room ID from URL parameters
    room_id = request.GET.get('id')
    
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country_code = request.POST.get('country_code')
        voucher_type = request.POST.get('voucher')
        
        # Get selected services
        services = []
        if request.POST.get('food_service'): services.append('Dịch Vụ Ăn Uống')
        if request.POST.get('laundry_service'): services.append('Dịch Vụ Giặt Là')
        if request.POST.get('transport_service'): services.append('Dịch Vụ Di Chuyển')
        if request.POST.get('entertainment_service'): services.append('Dịch Vụ Giải Trí và Thư Giãn')
        if request.POST.get('other_service'): services.append('Dịch Vụ Khác')

        # Calculate total price including services
        total_price = 0
        if room_id:
            try:
                room = Room.objects.get(id=room_id)
                total_price = room.price
                
                # Add service prices
                if 'Dịch Vụ Ăn Uống' in services: total_price += 150000
                if 'Dịch Vụ Giặt Là' in services: total_price += 50000
                if 'Dịch Vụ Di Chuyển' in services: total_price += 300000
                if 'Dịch Vụ Giải Trí và Thư Giãn' in services: total_price += 1200000
                
                # Create booking record
                booking = Booking.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    room=room,
                    name=name,
                    email=email,
                    phone=f"{country_code}{phone}",
                    voucher_type=voucher_type,
                    services=','.join(services),
                    total_price=total_price
                )
                
                messages.success(request, 'Đặt phòng thành công!')
                return redirect('booking_confirmation', booking_id=booking.id)
                
            except Room.DoesNotExist:
                messages.error(request, 'Phòng không tồn tại!')
                return redirect('rooms')
    
    # Get room details for display
    rooms = Room.objects.filter(id=room_id) if room_id else Room.objects.none()
    
    context = {
        'rooms': rooms,
        'user_not_login': user_not_login,
        'user_login': user_login
    }
    
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