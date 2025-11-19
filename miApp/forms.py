from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['rut_usuario']
        widgets = {
            'rut_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9'})
        }