from django.contrib import admin
from .models import Sala, Reserva

# Register your models here.

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'disponible')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'rut_usuario', 'fecha_inicio', 'fecha_termino')