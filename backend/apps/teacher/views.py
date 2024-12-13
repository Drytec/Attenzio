from django.shortcuts import render

# Create your views here.
import json
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

from .forms import TeacherRegisterForm
from django.db import IntegrityError
from django.utils import timezone
import pytz

from .models import Teacher
from ..session.forms import sessionForm


def home(request):
    print(request.user)
    return render(request,'core/home.html')
# esta es la funcion que valida que las vistas solo puedan ser accedidas por usuarios del tipo teacher
def is_teacher(user):
    return user.is_authenticated and hasattr(user, 'teacher')

@login_required
#se llama aca a la funcion
@user_passes_test(is_teacher)
def create_sesion(request):
    print(f'User ID: {request.user.id}')  # Esto debería imprimir el ID del usuario actual

    if request.method == 'GET':
        return render(request,'core/create_session.html',{
            'form':sessionForm
        })
    else:
        form = sessionForm(request.POST)
        if form.is_valid():
            new_session= form.save(commit=False)
            new_session.user = request.user
            new_session.save()
            return redirect('home')

        else:
            return render(request, 'core/create_session.html', {
                'form': form,
                'errors': form.errors
            })

def exit(request):
    logout(request)
    return redirect('home')

def teacher_singup_view(request):
    if request.method == 'GET':
        return render(request, 'core/signup.html', {
            'form': TeacherRegisterForm()
        })
    form = TeacherRegisterForm(request.POST, request.FILES)

    if form.is_valid():
        teacher = form.save(commit=False)

        teacher.username = f"{teacher.full_name}{teacher.teacher_document}{get_random_string(length=5)}"
        if Teacher.objects.filter(teacher_document=teacher.teacher_document).exists():
            form.add_error('documento', 'El documento ya existe. Por favor, utiliza otro.')
            return render(request, 'core/signup.html', {'form': form})

        if Teacher.objects.filter(email=teacher.email).exists():
            form.add_error('email', 'El correo ya existe. Por favor, utiliza otro.')
            return render(request, 'core/signup.html', {'form': form})

        teacher.validate = False

        teacher.password = make_password(form.cleaned_data['password'])

        try:
            teacher.save()
            login(request, teacher)
            return redirect('login')
        except IntegrityError as e:
            print(str(e))
            form.add_error(None, f'Ocurrió un error al guardar el profesor: {str(e)}')
            return render(request, 'core/signup.html', {'form': form})


    return render(request, 'core/signup.html', {'form': form})

def teacher_login_view(request):
    if request.method == 'GET':
        return render(request, 'core/login.html', {'form': AuthenticationForm()})

    elif request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, 'core/login.html', {
                'form': AuthenticationForm(),
                'error': 'Ambos campos son obligatorios'
            })

        # Autenticar al usuario
        user = authenticate(request, username=email, password=password)

        if user is None:
            return render(request, 'core/login.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrecto'
            })

        """if hasattr(user, 'validate') and not user.validate:
            return render(request, 'core/login.html', {
                'form': AuthenticationForm(),
                'error': 'Tu cuenta necesita ser validada por un administrador.'
            })"""

        # Iniciar sesión y redirigir
        login(request, user)
        return redirect('session')