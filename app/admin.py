from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost, Booking, Contact, Room, Promotion, Service

# Quản lý phòng
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'room_type', 'price', 'capacity', 'is_available', 'display_image')
    list_filter = ('room_type', 'is_available')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_available', 'price')
    ordering = ('id',)  # Sort by ID

    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('name', 'room_type', 'price', 'size', 'capacity')
        }),
        ('Mô tả và hình ảnh', {
            'fields': ('description', 'image')
        }),
        ('Trạng thái', {
            'fields': ('is_available',)
        }),
        ('Thông tin thời gian', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "Không có ảnh"
    display_image.short_description = "Hình ảnh"

admin.site.register(Room, RoomAdmin)

# Quản lý khuyến mãi
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'discount_percentage', 'start_date', 'end_date', 'is_active', 'limit', 'display_image')
    list_filter = ('is_active',)
    search_fields = ('code', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active', 'discount_percentage', 'limit')

    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('code', 'name', 'discount_percentage', 'limit')
        }),
        ('Thời gian khuyến mãi', {
            'fields': ('start_date', 'end_date')
        }),
        ('Hình ảnh và mô tả', {
            'fields': ('image', 'description')
        }),
        ('Trạng thái', {
            'fields': ('is_active',)
        }),
        ('Thông tin thời gian', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "Không có ảnh"
    display_image.short_description = "Hình ảnh"

admin.site.register(Promotion, PromotionAdmin)

# Thông tin liên hệ
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_resolved')
    list_filter = ('is_resolved', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Thông tin liên hệ', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Nội dung tin nhắn', {
            'fields': ('message',)
        }),
        ('Trạng thái', {
            'fields': ('is_resolved', 'created_at')
        }),
    )

    actions = ['mark_as_resolved']
    def mark_as_resolved(self, _request, queryset):
        queryset.update(is_resolved=True)
    mark_as_resolved.short_description = "Đánh dấu đã xử lý"

# Ensure Contact is registered only once
if not admin.site.is_registered(Contact):
    admin.site.register(Contact, ContactAdmin)

# Quản lý đặt phòng
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in', 'check_out', 'guests', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'check_in', 'check_out')
    search_fields = ('user__username', 'room__name')
    readonly_fields = ('created_at', 'updated_at', 'total_price')

    def save_model(self, request, obj, form, change):
        if not obj.total_price:
            obj.total_price = obj.calculate_total_price()
        super().save_model(request, obj, form, change)

# Ensure Booking is registered only once
if not admin.site.is_registered(Booking):
    admin.site.register(Booking, BookingAdmin)

# Quản lý bài viết
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(BlogPost, BlogPostAdmin)

# Quản lý dịch vụ
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
    fieldsets = (
        ('Thông tin dịch vụ', {
            'fields': ('name', 'price')
        }),
    )

admin.site.register(Service, ServiceAdmin)