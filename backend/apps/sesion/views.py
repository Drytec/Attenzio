import pytz
from django.contrib.auth import logout
from django.core.serializers import json
from .models import sesion
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import sesionForm
from django.db import IntegrityError
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login

# Create your views here.
# a este metodo de renderizado le falta la verificacion de la fecha la que esta aun no funciona

def sesion_interactive(request, sesion_id):
    colombia_tz = pytz.timezone('America/Bogota')
    ahora = timezone.now().astimezone(colombia_tz)
    sesion1 = get_object_or_404(sesion, sesion_id=sesion_id)
    if sesion1.date_start <= ahora <= sesion1.date_end:
        return render(request, 'core/sesion_online.html', {'sesion': sesion1})
    else:#  aqui lo mejor seria implementar un alertbox para que notifique que la clase no esta en horario
        return render(request, 'core/sesion.html')

@login_required
def sesion_class(request):
    #aqui nos aseguramos de que las aulas mostradas sean del profesor que hizo el login y las creo
    # tambien se realizan los filtros necesarios segun el caso
    sesion1 = sesion.objects.filter(user=request.user)
    return render(request,'core/sesion.html',{'sesion1': sesion1})


@login_required
def create_sesion(request):
    print(f'User ID: {request.user.id}')  # Esto debería imprimir el ID del usuario actual

    if request.method == 'GET':
        return render(request,'core/create_sesion.html',{
            'form':sesionForm
        })
    else:
        form = sesionForm(request.POST)
        if form.is_valid():
            new_aula= form.save(commit=False)
            new_aula.user = request.user
            new_aula.save()
            return redirect('home')

        else:
            return render(request, 'core/create_sesion.html', {
                'form': form,
                'errors': form.errors
            })

def exit(request):
    logout(request)
    return redirect('home')
