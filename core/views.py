from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
def home(request):
    return render(request,'core/home.html')

@login_required
def teachers(request):
    return render(request,'core/teachers.html')
def exit(request):
    logout(request)
    return redirect('home')
