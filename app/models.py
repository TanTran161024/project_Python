from django.db import models  
from django.contrib.auth import get_user_model  
from django.utils.text import slugify  
from django.db.models.signals import post_save  
from django.dispatch import receiver
from ckeditor.fields import RichTextField  
from datetime import datetime 
import uuid  



User = get_user_model()

class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Phòng đơn'),
        ('double', 'Phòng đôi'),
        ('suite', 'Phòng suite'),
        ('deluxe', 'Phòng cao cấp'),
    )
    name = models.CharField(max_length=200, verbose_name="Tên phòng")
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, verbose_name="Loại phòng")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá mỗi đêm (VNĐ)")
    size = models.IntegerField(help_text="Diện tích tính bằng mét vuông", verbose_name="Diện tích")
    service = models.CharField(max_length=200, verbose_name="Dịch vụ")
    capacity = models.IntegerField(help_text="Số khách tối đa", verbose_name="Sức chứa")
    description = RichTextField(verbose_name="Mô tả chi tiết")
    image = models.ImageField(upload_to='rooms/', verbose_name="Hình ảnh")
    is_available = models.BooleanField(default=True, verbose_name="Còn trống")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Phòng"
        verbose_name_plural = "Các phòng"

    def __str__(self):
        return f"{self.name} - {self.room_type}"
    
    def calculate_price_for_stay(self, nights):
        """Tính giá tổng cho số đêm ở"""
        return self.price * nights

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Đang chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('cancelled', 'Đã hủy'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', verbose_name="Người dùng")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings', verbose_name="Phòng đặt")
    check_in = models.DateField(verbose_name="Ngày nhận phòng")
    check_out = models.DateField(verbose_name="Ngày trả phòng")
    guests = models.IntegerField(verbose_name="Số lượng khách")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Trạng thái")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Tổng tiền (VNĐ)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đặt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Đặt phòng"
        verbose_name_plural = "Các đặt phòng"

    def __str__(self):
        return f"Đặt phòng {self.room.name} bởi {self.user.username}"
    
    def calculate_total_nights(self):
        """Tính tổng số đêm ở"""
        return (self.check_out - self.check_in).days
    
    def calculate_total_price(self):
        """Tính tổng giá dựa trên giá phòng và số đêm"""
        nights = self.calculate_total_nights()
        return self.room.calculate_price_for_stay(nights)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="Người dùng")
    phone = models.CharField(max_length=20, verbose_name="Số điện thoại")
    address = models.TextField(verbose_name="Địa chỉ")
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True, verbose_name="Ảnh đại diện")

    class Meta:
        verbose_name = "Hồ sơ người dùng"
        verbose_name_plural = "Hồ sơ người dùng"

    def __str__(self):
        return self.user.username
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    slug = models.SlugField(unique=True, verbose_name="Slug (đường dẫn)")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="Tác giả")
    content = RichTextField(verbose_name="Nội dung bài viết")
    image = models.ImageField(upload_to='blog/', verbose_name="Hình ảnh")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    is_published = models.BooleanField(default=False, verbose_name="Đã xuất bản")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Bài viết"
        verbose_name_plural = "Các bài viết"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Tự động tạo slug từ tiêu đề nếu chưa có"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """Trả về URL chi tiết của bài viết"""
        from django.urls import reverse
        return reverse('blog_detail', args=[str(self.slug)])
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Họ và tên")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Chủ đề")
    message = models.TextField(verbose_name="Nội dung tin nhắn")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày gửi")
    is_resolved = models.BooleanField(default=False, verbose_name="Đã xử lý")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Liên hệ"
        verbose_name_plural = "Các liên hệ"

    def __str__(self):
        return f"Tin nhắn từ {self.name}"
