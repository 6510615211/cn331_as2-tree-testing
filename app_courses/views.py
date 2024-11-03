from django.shortcuts import render, redirect, get_object_or_404
from app_courses.models import Subject

# Create your views here.

  
def courses(request):
    subjects = Subject.objects.all()  
    return render(request, "app_courses/courses.html", {"Subject":subjects})

   

def enroll_check(request):
    return render(request,'app_courses/enroll_check.html')

