from django.contrib import messages

from .models import Course, CustomUserCourse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CourseForm, CourseIdInputForm
from ..session.models import Session
from django.shortcuts import render, redirect

# Create your views here.
@login_required
def student_courses(request):
    if not request.user.isStudent:
        return redirect('home')

    course_ids = CustomUserCourse.objects.filter( custom_user_id=request.user.custom_user_id).values_list('course_id', flat=True)
    courses = Course.objects.filter(course_id__in=course_ids)

    courseTeachers = []
    for course in courses:
        try:
            teacher = CustomUserCourse.objects.filter(course_id=course.course_id, custom_user_id__is_teacher=True).select_related('custom_user_id').get()
            courseTeachers.append(teacher.custom_user_id)
        except CustomUserCourse.DoesNotExist:
            courseTeachers.append(None)

    return render(request,'student_courses.html',{'courses': courses, 'teachers': courseTeachers})

@login_required
def join_course(request):
    """
    Vista para mostrar el formulario de matriculación y realizar la inscripción al curso.

    """
    if not request.user.isStudent:
        return redirect('get_courses')

    if request.method == 'POST':
        form = CourseIdInputForm(request.POST)
        if form.is_valid():
            course_id = form.cleaned_data['course_id']
            course = Course.objects.filter(id=course_id).first()
            if course:
                if CustomUserCourse.objects.filter(custom_user_id=request.user, course_id=course).exists():
                    messages.error(request, 'Ya estás matriculado en este curso.')
                else:
                    CustomUserCourse.objects.create(
                        custom_user_id=request.user,
                        course_id=course
                    )
                    messages.success(request, 'Te has matriculado en el curso con éxito.')
                return redirect('get_courses')
            else:
                messages.error(request, 'El curso con este ID no existe.')
        else:
            messages.error(request, 'Por favor ingresa un ID de curso válido.')
    else:
        form = CourseIdInputForm()

    return render(request, 'join_course.html', {'form': form})

@login_required
def show_course(request, course_id):
    sessions = Session.objects.filter(course_id=course_id)
    course = get_object_or_404(Course, pk=course_id)
    customUserCourse = CustomUserCourse.objects.filter(course_id=course_id).first()
    teacher = customUserCourse.custom_user_id

    return render(request, 'show_course.html', {'course': course, 'sessions': sessions, 'teacher': teacher})

@login_required
def get_courses(request):
    course_ids = CustomUserCourse.objects.filter( custom_user_id=request.user.custom_user_id).values_list('course_id', flat=True)
    courses = Course.objects.filter(course_id__in=course_ids)

    return render(request,'courses.html',{'courses': courses})

@login_required
def create_course(request):
    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('student_courses')

    if request.method == 'GET':
        return render(request,'create_course.html',{
            'form':CourseForm
        })
    else:
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = request.user
            new_course.save()
            CustomUserCourse.objects.create(
                custom_user_id=request.user,
                course_id=new_course
            )

            return redirect('get_courses')


        else:
            return render(request, 'create_course.html', {
                'form': form,
                'errors': form.errors
            })

