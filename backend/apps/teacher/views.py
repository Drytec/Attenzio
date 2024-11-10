from django.shortcuts import render

# Create your views here.
import json

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

from .forms import TeacherForm
from django.db import IntegrityError
from django.utils import timezone
import pytz

from .models import Teacher
from ..sesion.forms import sesionForm


def home(request):
    print(request.user)
    return render(request,'core/home.html')
def register(request):
    return render(request,'core/signup.html',{
        'form':UserCreationForm
    })


@login_required
def create_aula(request):
    print(f'User ID: {request.user.id}')  # Esto debería imprimir el ID del usuario actual

    if request.method == 'GET':
        return render(request,'core/create_aula.html',{
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