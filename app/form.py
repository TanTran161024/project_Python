# forms.py
from django import forms
from .models import Promotion, Room

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['name', 'discount_percentage', 'start_date', 'end_date', 'image', 'description']
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'room_type', 'price', 'size', 'service', 'capacity', 'description', 'image', 'is_available']
