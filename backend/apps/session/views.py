import pytz
from django.contrib.auth import logout
from django.core.checks import messages
from django.core.serializers import json
from .models import Session
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import sessionForm
from django.db import IntegrityError
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login

# Create your views here.
# a este metodo de renderizado le falta la verificacion de la fecha la que esta aun no funciona
def session_interactive(request, session_id):
    colombia_tz = pytz.timezone('America/Bogota')
    ahora = timezone.now().astimezone(colombia_tz)
    session1 = get_object_or_404(Session, session_id=session_id)
    if session1.date_start <= ahora <= session1.date_end:
        return render(request, 'core/session_online.html', {'session': session1})
    else:#  aqui lo mejor seria implementar un alertbox para que notifique que la clase no esta en horario
        return render(request, 'core/session.html')

@login_required
def course_sessions(request):

    session1 = Session.objects.filter(user=request.user)
    return render(request,'core/session.html',{'session1': session1})

@login_required
def create_session(request):
    if not request.user.isTeacher():
        messages.error(request, "No tienes permiso para crear una sesión.")
        return render(request, 'student_courses.html')

    if request.method == 'GET':
        return render(request,'create_session.html',{
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
            return render(request, 'create_session.html', {
                'form': form,
                'errors': form.errors
            })

def exit(request):
    logout(request)
    return redirect('home')
