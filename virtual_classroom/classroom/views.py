from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'classroom/index.html')

def registerview(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Registered Successfully! Login to Continue'
            return redirect('/login')
    return render(request, 'classroom/auth/register.html', context={'form': form})

def loginview(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            msg = 'Logged in successfully'
            return redirect('/')
        else:
            msg = 'Invalid username or password'
            return redirect('/login')
    return render(request, 'classroom/auth/login.html')

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        msg = 'Logged out Successfully'
        return redirect('/')
    
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'classroom/class_list.html', {'classes': classes})

def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    discussions = lecture.discussions.all()
    form = DiscussionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        discussion = form.save(commit=False)
        discussion.user = request.user
        discussion.lecture = lecture
        discussion.save()
    return render(request, 'lecture_detail.html', {'lecture': lecture, 'discussions': discussions, 'form': form})

@login_required
def enroll_student(request):
    student, created = Student.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('class_detail')
    else:
        form = EnrollmentForm(instance=student)
    return render(request, 'classroom/enroll.html', {'form': form})


def my_enrollments(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    classrooms = [enrollment.classroom for enrollment in enrollments]
    
    context = {
        'classrooms': classrooms
    }
    return render(request, 'classroom/myenrollments.html', context)

