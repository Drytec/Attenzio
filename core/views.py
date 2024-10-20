from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from core.forms import aulaForm
from core.models import aula
from django.db import IntegrityError


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
