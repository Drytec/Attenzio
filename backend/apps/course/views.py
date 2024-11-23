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

# Create your views here.
# a este metodo de renderizado le falta la verificacion de la fecha la que esta aun no funciona

@login_required
def student_courses(request):
    if not request.user.isStudent():
        messages.error(request, "No tienes permiso para ver esto.")
        return render(request, 'teacher_courses.html')

    course = Course.objects.filter(user=request.user)
    return render(request,'student_courses.html',{'course': course})

@login_required
def show_course(request, course_id):
    colombia_tz = pytz.timezone('America/Bogota')
    ahora = timezone.now().astimezone(colombia_tz)
    course = get_object_or_404(Course, course_id=course_id)
    return render(request, 'show_course.html', {'course': course})


@login_required
def teacher_courses(request):
    if not request.user.isTeacher():
        messages.error(request, "No tienes permiso para ver esto.")
        return render(request, 'student_courses.html')

    course = Course.objects.filter(user=request.user)
    return render(request,'teacher_courses.html',{'course': course})


@login_required
def create_course(request):
    if not request.user.isTeacher():
        messages.error(request, "No tienes permiso para crear una sesión.")
        return render(request, 'teacher_courses.html')

    if request.method == 'GET':
        return render(request,'create_course.html',{
            'form':courseForm
        })
    else:
        form = courseForm(request.POST)
        if form.is_valid():
            new_session= form.save(commit=False)
            new_session.user = request.user
            new_session.save()
            return redirect('home')

        else:
            return render(request, 'core/create_course.html', {
                'form': form,
                'errors': form.errors
            })

def exit(request):
    logout(request)
    return redirect('home')
