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
from .forms import courseForm
from django.db import IntegrityError
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login

from ..customusercourse.models import CustomUserCourse
from ..session.models import Session


# Create your views here.
# a este metodo de renderizado le falta la verificacion de la fecha la que esta aun no funciona

@login_required
def student_courses(request):
    if not request.user.isStudent:
        messages.error(request, "No tienes permiso para ver esto.")
        return render(request, 'teacher_courses.html')

    user = request.user
    user_courses = CustomUserCourse.objects.filter(custom_user_id=user)

    return render(request,'student_courses.html',{'courses': user_courses})

@login_required
def show_course(request, course_id):
    sessions = Session.objects.filter(course_id=course_id)

    return render(request, 'course_sessions.html', {
        'sessions': sessions,
        'course_id': course_id,
    })

@login_required
def teacher_courses(request):
    if not request.user.isTeacher():
        messages.error(request, "No tienes permiso para ver esto.")
        return render(request, 'student_courses.html')

    user = request.user
    user_courses = CustomUserCourse.objects.filter(custom_user_id=user)

    return render(request,'teacher_courses.html',{'courses': user_courses})


@login_required
def create_course(request):
    if not request.user.isTeacher:
        messages.error(request, "No tienes permiso para crear una sesión.")
        return render(request, 'student_courses.html')

    if request.method == 'GET':
        return render(request,'create_course.html',{
            'form':courseForm
        })
    else:
        form = courseForm(request.POST)
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
            return render(request, 'core/create_course.html', {
                'form': form,
                'errors': form.errors
            })

def exit(request):
    logout(request)
    return redirect('home')
