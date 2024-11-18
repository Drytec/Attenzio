from django.shortcuts import render
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

from .forms import StudentRegisterForm
from django.db import IntegrityError
from django.utils import timezone
import pytz

from .models import Student
from ..session.forms import sessionForm

# Create your views here.
def home(request):
    print(request.user)
    return render(request,'core/home.html')

def exit(request):
    logout(request)
    return redirect('home')

def student_singup_view(request):
    if request.method == 'GET':
        return render(request, 'core/signup.html', {
            'form': StudentRegisterForm()
        })

    form = StudentRegisterForm(request.POST, request.FILES)

    if form.is_valid():
        student = form.save(commit=False)

        student.username = f"{student.full_name}{get_random_string(length=5)}"

        if Student.objects.filter(email=student.email).exists():
            form.add_error('email', 'El correo ya existe. Por favor, utiliza otro.')
            return render(request, 'core/signup.html', {'form': form})

        student.password = make_password(form.cleaned_data['password'])

        try:
            student.save()
            login(request, student)
            return redirect('login')

        except IntegrityError:
            form.add_error(None, 'Ocurrió un error al guardar el estudiante. Por favor, intenta nuevamente.')
            return render(request, 'core/signup.html', {'form': form})

    return render(request, 'core/signup.html', {'form': form})


def student_login_view(request):
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

        # Iniciar sesión y redirigir
        login(request, user)
        return redirect('session')
