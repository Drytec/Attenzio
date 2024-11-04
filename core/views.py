import json

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

from core.forms import aulaForm, TeacherForm
from core.models import aula, Teacher
from django.db import IntegrityError
from django.utils import timezone
import pytz

def home(request):
    print(request.user)
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
    print(f'User ID: {request.user.id}')  # Esto debería imprimir el ID del usuario actual

    if request.method == 'GET':
        return render(request,'core/create_aula.html',{
            'form':aulaForm
        })
    else:
        form = aulaForm(request.POST)
        if form.is_valid():
            new_aula= form.save(commit=False)
            new_aula.user = request.user
            new_aula.save()
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
        return render(request, 'core/signup.html', {
            'form': TeacherForm()
        })

    form = TeacherForm(request.POST, request.FILES)

    if form.is_valid():
        teacher = form.save(commit=False)

        # Asigna un valor único a username
        teacher.username = f"{teacher.nombre}{teacher.documento}{get_random_string(length=5)}"

        # Validar que documento y email sean únicos
        if Teacher.objects.filter(documento=teacher.documento).exists():
            form.add_error('documento', 'El documento ya existe. Por favor, utiliza otro.')
            return render(request, 'core/signup.html', {'form': form})

        if Teacher.objects.filter(email=teacher.email).exists():
            form.add_error('email', 'El correo ya existe. Por favor, utiliza otro.')
            return render(request, 'core/signup.html', {'form': form})

        # Cifra la contraseña y guarda el usuario
        teacher.password = make_password(form.cleaned_data['password'])

        try:
            teacher.save()
            login(request, teacher)
            return redirect('login1')

        except IntegrityError:
            form.add_error(None, 'Ocurrió un error al guardar el profesor. Por favor, intenta nuevamente.')
            return render(request, 'core/signup.html', {'form': form})

    return render(request, 'core/signup.html', {'form': form})

def login1(request):
    if request.method == 'GET':
        return render(request, 'core/login1.html', {
            'form': AuthenticationForm()
        })
    else:
        documento = request.POST['username']  # Usa 'documento' como nombre de usuario
        password = request.POST['password']
        user = authenticate(request, username=documento, password=password)
        if user is None:
            return render(request, 'core/login1.html', {
                'form': AuthenticationForm(), 'error': 'Usuario o Contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('aula')

# a este metodo de renderizado le falta la verificacion de la fecha la que esta aun no funciona
def aula_interactive(request, aula_id):
    print(aula_id)
    colombia_tz = pytz.timezone('America/Bogota')
    ahora = timezone.now().astimezone(colombia_tz)
    aula1 = get_object_or_404(aula, aula_id=aula_id)
    if aula1.fecha_inicio <= ahora <= aula1.fecha_fin:
        return render(request, 'core/aula_online.html', {'aula1': aula1})
    else:#  aqui lo mejor seria implementar un alertbox para que notifique que la clase no esta en horario
        return render(request, 'core/aula.html')

@csrf_exempt
@login_required
#este es un metodo para renderizar el aula pero tiene muchos fallos
def aula_online(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            aula_id = data.get('aula_id')
            colombia_tz = pytz.timezone('America/Bogota')
            ahora = timezone.now().astimezone(colombia_tz)

            # Obtener el aula correspondiente al ID proporcionado
            aula_selected = get_object_or_404(aula, aula_id=aula_id, user=request.user)

            # Depuración de horarios
            print("Ahora:", ahora)
            print("Fecha de inicio:", aula_selected.fecha_inicio.astimezone(colombia_tz))
            print("Fecha de fin:", aula_selected.fecha_fin.astimezone(colombia_tz))

            # Verificar el horario
            if aula_selected.fecha_inicio <= ahora <= aula_selected.fecha_fin:
                # Redirigir a la plantilla con el aula seleccionada
                return render(request, 'core/aula_online.html', {
                   'aula' :aula_selected
                })
            else:
                return JsonResponse({'success': False, 'error': 'La clase no está en horario.'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Error al decodificar el JSON.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request, 'core/aula_online.html')
