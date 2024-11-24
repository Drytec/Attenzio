from django.contrib import messages
from django.shortcuts import render

import json
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

from .forms import TeacherRegisterForm, StudentRegisterForm
from .models import isTeacher
from django.db import IntegrityError
from django.utils import timezone
import pytz
from .models import CustomUser

from ..session.forms import sessionForm


def home(request):
    print(request.user)
    return render(request, 'core/home.html')

def exit(request):
    logout(request)
    return redirect('home')

def select_user_type_view(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type in ['student', 'teacher']:
            return redirect(f'/signup/?type={user_type}')
    return render(request, 'core/select_user_type.html')

def user_singup_view(request):
    user_type = request.GET.get('type', None)

    if user_type == 'teacher':
        form_class = TeacherRegisterForm
    else:
        form_class = StudentRegisterForm

    if request.method == 'GET':
        form = form_class()
        return render(request, 'core/signup.html', {'form': form, 'user_type': user_type})

    form = form_class(request.POST, request.FILES)
    if form.is_valid():
        user = form.save()
        return redirect('login')

    return render(request, 'core/signup.html', {'form': form, 'user_type': user_type})


def user_login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'core/login.html', {'form': form})

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

        """if not user.validate:
            return render(request, 'core/login.html', {
                'form': AuthenticationForm(),
                'error': 'Tu cuenta necesita ser validada por un administrador.'
            })"""

        # Iniciar sesión y redirigir
        login(request, user)
        return redirect('course')