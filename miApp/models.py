from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    rut_usuario = models.CharField(max_length=12)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.fecha_termino:
            self.fecha_termino = timezone.now() + datetime.timedelta(hours=2)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Reserva de {self.rut_usuario} - {self.sala}"