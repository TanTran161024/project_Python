from django.contrib import admin

from django.urls import path
from . import views
from .views import signup

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup,name='signup'),
    path('about-us/', views.about, name='about-us'),
    path('contact/', views.contact, name='contact'),
    path('main/', views.main, name='main'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('rooms/', views.rooms, name='rooms'),
    path('room-details/', views.roomdetail, name='room-details'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blogdetail, name='blog-details'),
    path('pages/', views.pages, name='pages'),
    path('booking/', views.booking, name='booking'),
    path('promotion/', views.promotion, name='promotion'),
    path('manage-promotions/', views.manage_promotions, name='manage_promotions'),
    path('promotion/edit/<int:id>/', views.edit_promotion, name='promotion_edit'),
    path('promotion/delete/<int:id>/', views.delete_promotion, name='promotion_delete'),
    path('manage-room/', views.manage_room, name='manage_room'),
    path('room/delete/<int:id>/', views.delete_room, name='room_delete'),
    path('room/add/', views.add_room, name='add_room'),
    path('room/edit/<int:id>/', views.edit_room, name='edit_room'),
    path('check-in/', views.check_in_view, name='check_in'),
    path('check-out/', views.check_out_view, name='check_out'),
    path('thongkedoanhthu/', views.thongkedoanhthu, name='thongkedoanhthu'),

]