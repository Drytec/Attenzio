from django.contrib.auth import logout
from django.urls import reverse

from .models import Session, MaterialSession, Question, Material, Option, CustomUserOption
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SessionForm, QuestionForm, MaterialForm, OptionForm
from django.shortcuts import render, redirect
from ..course.models import Course, CustomUserCourse


# Create your views here.

import qrcode
from django.http import HttpResponse
from io import BytesIO

@login_required
def show_session(request, session_id):
    session = get_object_or_404(Session, session_id=session_id)
    materials = Material.objects.filter(materialsession__session_id=session_id)

    # Generar el código QR
    url = request.build_absolute_uri(reverse('answer_questions', args=[session_id]))
    img = qrcode.make(url)
    qr_io = BytesIO()
    img.save(qr_io, 'PNG')
    qr_io.seek(0)
    qr_image = qr_io.getvalue()

    return render(request, 'show_session.html', {
        'session': session,
        'materials': materials,
        'qr_image': qr_image
    })


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

    if request.method == 'GET':
        return render(request,'create_session.html',{
            'form': SessionForm, 'course': course,
        })
    else:
        form = SessionForm(request.POST)
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

        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            new_question.session_id = session
            new_question.user = request.user
            new_question.save()

            return redirect('choose_num_options', session_id=session_id, question_id=new_question.question_id)

        else:
            return render(request, 'create_question.html', {
                'question_form': question_form,
                'session': session,
            })

    else:
        question_form = QuestionForm()
        return render(request, 'create_question.html', {
            'question_form': question_form,
            'session': session
        })

@login_required
def choose_num_options(request, session_id, question_id):
    session = get_object_or_404(Session, pk=session_id)
    question = get_object_or_404(Question, pk=question_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    if request.method == 'POST':
        num_options = int(request.POST.get('num_options', 4))

        return redirect('create_options', session_id=session_id, question_id=question_id, num_options=num_options)

    return render(request, 'choose_num_options.html', {
        'question': question,
        'session': session
    })

@login_required
def show_questions(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    questions = Question.objects.filter(session_id=session_id)

    return render(request, 'show_questions.html', {'questions': questions, 'session': session})

@login_required
def show_options(request, session_id, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=question.session_id)

    options = Option.objects.filter(question_id=question_id)
    return render(request, 'show_options.html', {'options': options})

@login_required
def create_options(request, session_id, question_id, num_options):
    session = get_object_or_404(Session, pk=session_id)
    question = get_object_or_404(Question, pk=question_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    form_options = [OptionForm(prefix=f"option_{i}") for i in range(num_options)]

    if request.method == 'POST':
        for form in form_options:
            form = OptionForm(request.POST, prefix=form.prefix)
            if form.is_valid():
                option = form.save(commit=False)
                option.question_id = question
                option.save()

        return redirect('show_session', session_id=session_id)

    return render(request, 'create_options.html', {
        'question': question,
        'session': session,
        'form_options': form_options,
        'num_options': num_options
    })

@login_required
def answer_questions(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    questions = Question.objects.filter(session_id=session_id)

    selected_options = {}

    if request.method == 'POST':
        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.question_id}')
            if selected_option_id:
                option = get_object_or_404(Option, pk=selected_option_id)
                CustomUserOption.objects.create(
                    custom_user_id=request.user,
                    option_id=option
                )

        return redirect('show_session', session_id=session_id)

    return render(request, 'answer_questions.html', {
        'session': session,
        'questions': questions,
    })

def exit(request):
    logout(request)
    return redirect('home')
