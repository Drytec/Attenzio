import pytz
from django.contrib.auth import logout
from django.core.checks import messages
from django.core.serializers import json
from .models import Session, MaterialSession, Question, Material
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import SessionForm, QuestionForm, MaterialForm, OptionFormSet
from django.db import IntegrityError
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login

from ..course.models import Course


# Create your views here.

@login_required
def show_session(request, session_id):
    session = get_object_or_404(Session, session_id=session_id)
    materials = session.sessionMaterial.all()

    return render(request, 'show_session.html', {'session': session, 'materials': materials})


@login_required
def create_session(request, course_id):
    if not request.user.isTeacher:
        messages.error(request, "No tienes permiso para crear una sesión.")
        return render(request, 'student_courses.html')

    course = get_object_or_404(Course, course_id=course_id)
    print(course_id)
    if request.method == 'GET':
        return render(request,'create_session.html',{
            'form': SessionForm, 'course': course,
        })
    else:
        form = SessionForm(request.POST)
        print(course_id)
        if form.is_valid():
            new_session = form.save(commit=False)
            new_session.course_id = course
            new_session.user = request.user
            new_session.save()
            session_id = new_session.session_id
            return redirect('show_session', session_id=session_id)

        else:
            return render(request, 'create_session.html', {
                'form': form,
                'errors': form.errors
            })

def create_material(request, session_id):
    if not request.user.isTeacher:
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
    if not request.user.isTeacher:
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
    if not request.user.isTeacher:
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
