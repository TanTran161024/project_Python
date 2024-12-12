from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('login/', views.login_view, name='login'),
    path('rooms/', views.rooms, name='rooms'),
    path('signup/', views.signup, name='signup'),
]