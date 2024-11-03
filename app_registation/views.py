from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def home(request):
    return render(request,'app_registation/home.html')

def about(request):
    return render(request,'app_registation/about.html')
    
def enroll_check(request):
    return render(request,'app_registation/enroll_check.html')

  