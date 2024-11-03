from django.db import models
from django.core.exceptions import ValidationError

class Subject(models.Model):
    
    class CourseStatus(models.TextChoices):
        AVAILABLE = 'Available', 'Available'
        REGISTERED = 'Registered', 'Registered'
        FULL = 'Full', 'Full'
    
    course_id = models.CharField(max_length=100, unique=True)
    course_name = models.CharField(max_length=100)
    course_semester = models.CharField(max_length=100)
    course_amount = models.IntegerField(default=0)
    course_status = models.CharField(
        max_length=15,
        choices=CourseStatus.choices,
        default=CourseStatus.AVAILABLE,
    )
    
    def clean(self):
        if self.course_amount < 0:
            raise ValidationError('Course amount cannot be negative.')

    def __str__(self):
        return f"{self.course_id} {self.course_name} {self.course_semester} STATUS: {self.course_status}"

class Student(models.Model):
    student_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    enrolled_subjects = models.ManyToManyField(Subject, related_name='students', blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
