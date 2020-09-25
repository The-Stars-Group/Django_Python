from django import forms
from .models import Kiosk

class KioskForm(forms.ModelForm):
    class Meta:
        model = Kiosk
        fields = '__all__'