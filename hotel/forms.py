from django.contrib.auth.forms import forms
from hotel.models import hotel

class hotelform(forms.modelForm):
    class Meta:
        model=hotel
        
        fields={
            'hotel_id',
            'hotel_name',
            'hotel_location',
            'hotel_star'
        }
