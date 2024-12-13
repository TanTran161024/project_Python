from django.contrib import admin
from .models import BlogPost, Booking, Contact, Room, UserProfile

# Đăng ký các mô hình vào Django Admin
admin.site.register(BlogPost)
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(UserProfile)
