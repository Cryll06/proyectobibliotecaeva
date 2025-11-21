from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    rut_usuario = forms.CharField(
        label="RUT",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Ej: 12.345.678-9'
        })
    )

    class Meta:
        model = Reserva
        fields = ['rut_usuario']

    def clean_rut_usuario(self):
        rut = self.cleaned_data.get('rut_usuario')

        if len(rut) < 8:
            raise forms.ValidationError("El RUT no es válido")


        if '-' not in rut:
            raise forms.ValidationError("El RUT no es válido")
            
        return rut