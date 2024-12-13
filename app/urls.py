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
    path('login/', views.login, name='login'),
    path('rooms/', views.rooms, name='rooms'),
    path('room-details/', views.roomdetail, name='room-details'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blogdetail, name='blog-details'),
    path('pages/', views.pages, name='pages'),
    path('booking/', views.booking, name='booking'),
]