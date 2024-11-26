import pytz
from django.contrib.auth import logout
from django.core.checks import messages
from django.core.serializers import json
from .models import Session, SessionMaterial, Question
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import SessionForm, QuestionForm, OptionForm, MaterialForm, OptionFormSet
from django.db import IntegrityError
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login

from ..course.models import Course


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
def show_session(request, session_id):
    session = get_object_or_404(Session, session_id=session_id)
    material = session.sessionMaterial.all()

    return render(request, 'show_session.html', {'session': session, 'material': material})


@login_required
def create_session(request, course_id):
    if not request.user.isTeacher():
        messages.error(request, "No tienes permiso para crear una sesión.")
        return render(request, 'student_courses.html')

    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'GET':
        return render(request,'create_session.html',{
            'form': SessionForm,
        })
    else:
        form = SessionForm(request.POST)
        if form.is_valid():
            new_session = form.save(commit=False)
            new_session.course_id = course
            new_session.user = request.user
            new_session.save()
            session_id = new_session.session_id
            return redirect('create_material', session_id=session_id)

        else:
            return render(request, 'create_session.html', {
                'form': form,
                'errors': form.errors
            })

def create_material(request, session_id):
    if not request.user.isTeacher():
        messages.error(request, "No tienes permiso para crear material.")
        return render(request, 'student_courses.html')

    session = get_object_or_404(Session, pk=session_id)

    if request.method == 'GET':
        return render(request,'create_material.html',{
            'form': MaterialForm,
        })
    else:
        form = MaterialForm(request.POST)
        if form.is_valid():
            new_material = form.save(commit=False)
            new_material.user = request.user
            new_material.save()
            SessionMaterial.objects.create(
                session_id=session_id,
                material_id=new_material.material_id
            )
            course_id = session.course_id
            return redirect('show_course', course_id=course_id)

        else:
            return render(request, 'create_material.html', {
                'form': form,
                'errors': form.errors
            })

def create_question(request, session_id):
    if not request.user.isTeacher():
        messages.error(request, "No tienes permiso para crear preguntas.")
        return render(request, 'student_courses.html')

    session = get_object_or_404(Session, pk=session_id)

    if request.method == 'GET':
        return render(request,'create_question.html',{
            'form': QuestionForm,
        })
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.session_id = session
            new_question.user = request.user
            new_question.save()
            question_id = new_question.question_id
            return redirect('create_options', question_id=question_id)

        else:
            return render(request, 'create_material.html', {
                'form': form,
                'errors': form.errors
            })

def create_options(request, question_id):
    if not request.user.isTeacher():
        messages.error(request, "No tienes permiso para crear opciones.")
        return render(request, 'student_courses.html')

    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'GET':
        return render(request,'create_options.html',{
            'formset': OptionFormSet,
        })
    else:
        formset = OptionFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                new_option = form.save(commit=False)
                new_option.question_id = question
                new_option.user = request.user
                new_option.save()
                session_id = question.session_id
            return redirect('show_session', session_id=session_id)

        else:
            return render(request, 'create_options.html', {
                'formset': formset,
                'errors': formset.errors
            })

def exit(request):
    logout(request)
    return redirect('home')
