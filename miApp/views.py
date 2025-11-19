from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Sala, Reserva
from .forms import ReservaForm

# Create your views here.

def lista_salas(request):
    reservas_vencidas = Reserva.objects.filter(fecha_termino__lt=timezone.now())
    for reserva in reservas_vencidas:
        if not reserva.sala.disponible:
            reserva.sala.disponible = True
            reserva.sala.save()

    salas = Sala.objects.all()
    return render(request, 'lista_salas.html', {'salas': salas})

def detalle_sala(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    reserva_activa = Reserva.objects.filter(sala=sala, fecha_termino__gt=timezone.now()).last()
    
    if request.method == 'POST' and sala.disponible:
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.sala = sala
            reserva.save()
            
            sala.disponible = False
            sala.save()
            return redirect('lista_salas')
    else:
        form = ReservaForm()

    return render(request, 'detalle_sala.html', {
        'sala': sala, 
        'form': form, 
        'reserva_activa': reserva_activa
    })