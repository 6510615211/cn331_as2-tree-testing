from django.shortcuts import render
from django.http.response import HttpResponse
from app_courses.models import Subject
# Create your views here.


def courses(request):
    subjects = Subject.objects.all()
    return render(request, "app_courses/courses.html", {"subjects":subjects})