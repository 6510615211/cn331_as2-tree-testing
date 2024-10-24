from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from app_courses.models import Subject

# Create your views here.

  
def courses(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')

        
        subject = get_object_or_404(Subject, id=subject_id)
        subject.course_status = "REGISTERED"
        subject.course_amount -= 1
        subject.save()

        #return redirect('courses')    
    return render(request, "app_courses/courses.html", {"Subject":subjects})



'''def enroll_check(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject = get_object_or_404(Subject, id=subject_id)
        
        #course_name = request.POST.get('course_name')  
        #semester = request.POST.get('semester')  

        if subject_id:
            
            subject = get_object_or_404(Subject, id=subject_id)
        return redirect('courses')
    return render(request,'app_courses/enroll_check.html')'''
    

def enroll_check(request):
    return render(request,'app_courses/enroll_check.html')