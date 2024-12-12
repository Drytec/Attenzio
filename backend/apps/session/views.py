import pytz
from django.contrib.auth import logout
from django.core.checks import messages
from django.core.serializers import json
from django.forms import modelformset_factory

from .models import Session, MaterialSession, Question, Material, Option
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import SessionForm, QuestionForm, MaterialForm, OptionFormSet, OptionForm
from django.db import IntegrityError
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login

from ..course.models import Course
from ..customusercourse.models import CustomUserCourse


# Create your views here.

@login_required
def show_session(request, session_id):
    session = get_object_or_404(Session, session_id=session_id)
    materials = Material.objects.filter(materialsession__session_id=session_id)

    return render(request, 'show_session.html', {'session': session, 'materials': materials})

@login_required
def report_view(request, custom_user_id, course_id):
    custom_user_course = get_object_or_404(
        CustomUserCourse,
        custom_user_id=custom_user_id,
        course_id=course_id
    )

    custom_user = custom_user_course.custom_user_id
    course = custom_user_course.course_id

    sesiones = Session.objects.filter(course_id=course).distinct()

    show_report = 'generate_report' in request.GET

    context = {
        'custom_user': custom_user,
        'course': course,
        'sesiones': sesiones,
        'show_report': show_report,
    }

    return render(request, 'show_session.html', context)


@login_required
def create_session(request, course_id):
    if not request.user.isTeacher:
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

@login_required
def create_material(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return render(request, 'student_courses.html', {'session': session})

    session = get_object_or_404(Session, pk=session_id)

    if request.method == 'GET':
        return render(request,'create_material.html',{
            'form': MaterialForm,
            'session': session
        })
    else:
        form = MaterialForm(request.POST)
        if form.is_valid():
            new_material = form.save(commit=False)
            new_material.user = request.user
            new_material.save()
            MaterialSession.objects.create(
                session_id=session,
                material_id=new_material
            )
            return redirect('show_session', session_id=session.session_id)

        else:
            return render(request, 'create_material.html', {
                'form': form,
                'errors': form.errors,
                'session': session
            })

@login_required
def create_question(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        num_options = int(request.POST.get('num_options', 4))

        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            new_question.session_id = session
            new_question.user = request.user
            new_question.save()

            return redirect('create_options', session_id=session_id, question_id=new_question.question_id, num_options=num_options)

        else:
            return render(request, 'create_question.html', {
                'question_form': question_form,
                'session': session,
                'num_options': num_options
            })

    else:
        question_form = QuestionForm()
        return render(request, 'create_question.html', {
            'question_form': question_form,
            'session': session
        })

@login_required
def show_questions(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    questions = Question.objects.filter(session_id=session_id)

    return render(request, 'show_questions.html', {'questions': questions})

@login_required
def show_options(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=question.session_id)

    options = Option.objects.filter(question_id=question_id)

    return render(request, 'show_options.html', {'options': options})

@login_required
def create_options(request, session_id, question_id, num_options):
    question = get_object_or_404(Question, pk=question_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    if request.method == 'GET':
        OptionFormSet = modelformset_factory(Option, form=OptionForm, extra=num_options)
        formset = OptionFormSet(queryset=Option.objects.none())

        return render(request, 'create_options.html', {
            'question': question,
            'formset': formset,
            'num_options': num_options
        })

    else:
        OptionFormSet = modelformset_factory(Option, form=OptionForm, extra=num_options)
        formset = OptionFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                new_option = form.save(commit=False)
                new_option.question_id = question
                new_option.user = request.user
                new_option.save()

            return redirect('show_session', session_id=session_id)

        else:
            return render(request, 'create_options.html', {
                'question': question,
                'formset': formset,
                'errors': formset.errors,
                'num_options': num_options
            })

def exit(request):
    logout(request)
    return redirect('home')
