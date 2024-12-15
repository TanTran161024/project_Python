# Generated by Django 5.1.4 on 2024-12-15 04:36

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Họ và tên')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=200, verbose_name='Chủ đề')),
                ('message', models.TextField(verbose_name='Nội dung tin nhắn')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày gửi')),
                ('is_resolved', models.BooleanField(default=False, verbose_name='Đã xử lý')),
            ],
            options={
                'verbose_name': 'Liên hệ',
                'verbose_name_plural': 'Các liên hệ',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Tên phòng')),
                ('room_type', models.CharField(choices=[('single', 'Phòng đơn'), ('double', 'Phòng đôi'), ('suite', 'Phòng suite'), ('deluxe', 'Phòng cao cấp')], max_length=20, verbose_name='Loại phòng')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Giá mỗi đêm (VNĐ)')),
                ('size', models.IntegerField(help_text='Diện tích tính bằng mét vuông', verbose_name='Diện tích')),
                ('service', models.CharField(max_length=200, verbose_name='Dịch vụ')),
                ('capacity', models.IntegerField(help_text='Số khách tối đa', verbose_name='Sức chứa')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Mô tả chi tiết')),
                ('image', models.ImageField(upload_to='rooms/', verbose_name='Hình ảnh')),
                ('is_available', models.BooleanField(default=True, verbose_name='Còn trống')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')),
            ],
            options={
                'verbose_name': 'Phòng',
                'verbose_name_plural': 'Các phòng',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tiêu đề')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug (đường dẫn)')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Nội dung bài viết')),
                ('image', models.ImageField(upload_to='blog/', verbose_name='Hình ảnh')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')),
                ('is_published', models.BooleanField(default=False, verbose_name='Đã xuất bản')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='Tác giả')),
            ],
            options={
                'verbose_name': 'Bài viết',
                'verbose_name_plural': 'Các bài viết',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(verbose_name='Ngày nhận phòng')),
                ('check_out', models.DateField(verbose_name='Ngày trả phòng')),
                ('guests', models.IntegerField(verbose_name='Số lượng khách')),
                ('status', models.CharField(choices=[('pending', 'Đang chờ xác nhận'), ('confirmed', 'Đã xác nhận'), ('cancelled', 'Đã hủy')], default='pending', max_length=20, verbose_name='Trạng thái')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tổng tiền (VNĐ)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày đặt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL, verbose_name='Người dùng')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='app.room', verbose_name='Phòng đặt')),
            ],
            options={
                'verbose_name': 'Đặt phòng',
                'verbose_name_plural': 'Các đặt phòng',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Số điện thoại')),
                ('address', models.TextField(verbose_name='Địa chỉ')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='Ảnh đại diện')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Người dùng')),
            ],
            options={
                'verbose_name': 'Hồ sơ người dùng',
                'verbose_name_plural': 'Hồ sơ người dùng',
            },
        ),
    ]