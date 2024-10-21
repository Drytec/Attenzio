import json

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from core.forms import aulaForm
from core.models import aula
from django.db import IntegrityError
from django.utils import timezone
import pytz

def home(request):
    return render(request,'core/home.html')
def register(request):
    return render(request,'core/signup.html',{
        'form':UserCreationForm
    })
@login_required
def aula_class(request):
    #aqui nos aseguramos de que las aulas mostradas sean del profesor que hizo el login y las creo
    # tambien se realizan los filtros necesarios segun el caso
    aula1 = aula.objects.filter(user=request.user)
    return render(request,'core/aula.html',{'aula1': aula1})
@login_required
def create_aula(request):
    if request.method == 'GET':
        return render(request,'core/create_aula.html',{
            'form':aulaForm
        })
    else:
        form = aulaForm(request.POST)
        if form.is_valid():

            print(form)
            new_aula= form.save(commit=False)
            new_aula.user = request.user
            new_aula.save()
            #hay que programar a donde nos va a redirigir despues de crear la tarea
            return redirect('home')

        else:
            return render(request, 'core/create_aula.html', {
                'form': form,
                'errors': form.errors
            })

def exit(request):
    logout(request)
    return redirect('home')
def signup(request):
    if request.method == 'GET':
        return render(request,'core/signup.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registra usuario
            # est Usuario será un profesor que haga el registro, aún hay que hacer que el admin apruebe su ingreso
            # por ahora esta recibiendo y creandose con un objeto tipo user, hay que cambiarlo a uno teacher
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('login1')
            except IntegrityError:
                return render(request, 'core/signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })
        else:
            return render(request, 'core/signup.html', {
                'form': UserCreationForm,
                "error": 'Las contraseñas no coinciden'
            })
def login1(request):
    if request.method == 'GET':
        return render(request,'core/login1.html',{
            'form':AuthenticationForm
        })
    else:
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
             return render(request,'core/login1.html',{
            'form':AuthenticationForm, 'error' : 'Usuario o Contraseña incorrecto'})
        else:
            login(request, user)
            return redirect('aula')
@csrf_exempt
@login_required
def aula_online(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            aula_id = data.get('aula_id')
            colombia_tz = pytz.timezone('America/Bogota')
            ahora = timezone.now().astimezone(colombia_tz)

            aula_selected = get_object_or_404(aula, aula_id=aula_id, user=request.user)

            # Agrega estos prints para depurar
            print("Ahora:", ahora)
            print("Fecha de inicio:", aula_selected.fecha_inicio.astimezone(colombia_tz))
            print("Fecha de fin:", aula_selected.fecha_fin.astimezone(colombia_tz))

            if aula_selected.fecha_inicio <= ahora <= aula_selected.fecha_fin:
                return JsonResponse({'success': True, 'redirect_url': '/aula/online/'})
            else:
                return JsonResponse({'success': False, 'error': 'La clase no está en horario.'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Error al decodificar el JSON.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request, 'core/aula_online.html')
