import pytz
from django.contrib import messages
from django.contrib.auth import logout
from django.core.serializers import json
from .models import Course
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import CourseForm
from django.db import IntegrityError
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login

from ..customusercourse.models import CustomUserCourse


# Create your views here.
# a este metodo de renderizado le falta la verificacion de la fecha la que esta aun no funciona

@login_required
def student_courses(request):
    if not request.user.isStudent:
        messages.error(request, "No tienes permiso para ver esto.")
        return render(request, 'teacher_courses.html')

    course = request.user.getCourses

    return render(request,'student_courses.html',{'course': course})

@login_required
def show_session_course(request, course_id):
    # esta es la funcion a la que se llama cuando se presiona en un curso,
    # tiene que renderizar las sesiones que hayan sido creadas
    session = get_object_or_404(Session, course_id=course_id)
    return render(request, 'show_course.html', {'course': course})


@login_required
def teacher_courses(request):
    # esto se comenta ya que la funcion isTeacher no ha sido bien configuratda
    #if not request.user.isTeacher():
     #   messages.error(request, "No tienes permiso para ver esto.")
      #  return render(request, 'student_courses.html')
    coursesTeacher=CustomUserCourse.objects.filter( custom_user_id=request.user.custom_user_id)
    #ponemos flat para aplanar la lista
    course_ids = coursesTeacher.values_list('course_id', flat=True)
    #el __in que se le agrega a course es para que django tome todos los valores relacionados y no un unico id
    courses = Course.objects.filter(course_id__in=course_ids)
    print(courses)

    return render(request,'teacher_courses.html',{'courses': courses})


@login_required
def create_course(request):
    if not request.user.isTeacher:
        messages.error(request, "No tienes permiso para crear una sesión.")
        return render(request, 'student_courses.html')

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
            return redirect('home')

        else:
            return render(request, 'create_course.html', {
                'form': form,
                'errors': form.errors
            })

