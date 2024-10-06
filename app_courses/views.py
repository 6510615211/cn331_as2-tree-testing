from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def courses(request):
    return render(request, 'app_courses/courses.html')
