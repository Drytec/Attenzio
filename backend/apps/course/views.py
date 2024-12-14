from django.contrib import messages
from .models import Course, CustomUserCourse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CourseForm, CourseIdInputForm
from ..session.models import Session
from django.shortcuts import render, redirect

# Create your views here.

@login_required
def join_course(request):
    """
    Vista para mostrar el formulario de matriculación y permitir que el estudiante se inscriba en un curso.

    - Verifica que el usuario sea un estudiante antes de permitir la inscripción.
    - Si el curso existe y el estudiante no está matriculado, se realiza la inscripción.
    - Muestra mensajes de éxito o error dependiendo del estado de la inscripción.

    Retorna:
    - La plantilla `join_course.html` con el formulario de inscripción al curso.
    """
    if not request.user.isStudent:
        return redirect('get_courses')

    if request.method == 'POST':
        form = CourseIdInputForm(request.POST)
        if form.is_valid():
            course_id = form.cleaned_data['course_id']
            course = Course.objects.filter(pk=course_id).first()
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
    """
    Vista para mostrar los detalles de un curso específico, incluyendo las sesiones y el profesor.

    - Recupera el curso, las sesiones asociadas y el profesor encargado del curso.

    Parámetros:
    - course_id: ID del curso a mostrar.

    Retorna:
    - La plantilla `show_course.html` con los detalles del curso, las sesiones y el profesor.
    """
    sessions = Session.objects.filter(course_id=course_id)
    course = get_object_or_404(Course, pk=course_id)
    customUserCourse = CustomUserCourse.objects.filter(course_id=course_id).first()
    teacher = customUserCourse.custom_user_id

    return render(request, 'show_course.html', {'course': course, 'sessions': sessions, 'teacher': teacher})

@login_required
def get_courses(request):
    """
    Vista que muestra los cursos a los que el usuario está matriculado.

    - Recupera los cursos asociados al usuario a través de la relación con `CustomUserCourse`.

    Retorna:
    - La plantilla `courses.html` con la lista de cursos.
    """
    course_ids = CustomUserCourse.objects.filter(custom_user_id=request.user.custom_user_id).values_list('course_id', flat=True)
    courses = Course.objects.filter(course_id__in=course_ids)

    return render(request, 'courses.html', {'courses': courses})

@login_required
def create_course(request):
    """
    Vista para crear un nuevo curso, solo accesible para profesores y administradores.

    - Verifica que el usuario sea un profesor o administrador antes de permitir la creación del curso.
    - Si el formulario es válido, crea el curso y lo asocia con el usuario actual.
    - Muestra el formulario de creación de curso y los errores si el formulario no es válido.

    Retorna:
    - La plantilla `create_course.html` con el formulario de creación del curso.
    """
    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('student_courses')

    if request.method == 'GET':
        return render(request, 'create_course.html', {
            'form': CourseForm
        })
    else:
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = request.user  # Asocia el curso con el usuario actual (profesor)
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


