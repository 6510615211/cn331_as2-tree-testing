from django.db import models

# Create your models here.
class Subject(models.Model):
    
    class CourseStatus(models.TextChoices):
        AVAIABLE = 'Avaiable', 'Avaiable'
        REGISTERED = 'Registered', 'Registered'
        FULL = 'Full', 'Full'
    course_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_semester = models.CharField(max_length=100)
    course_amount = models.IntegerField(default=0)
    course_status = models.CharField(
        max_length=10,
        choices=CourseStatus.choices,
        default=CourseStatus.AVAIABLE,
    )
    def __str__(self):
        return self.course_id +' '+ self.course_name +' '+ self.course_semester +' '+ 'STATUS : ' + self.course_status
    
    
class Student(models.Model):
    student_id = models.CharField(max_length=100)
    enrolled_subjects = models.ManyToManyField(Subject, related_name='students', blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"