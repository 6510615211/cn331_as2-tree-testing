from django.db import models

# Create your models here.
class Subject(models.Model):
    course_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_semester = models.CharField(max_length=100)
    course_amount = models.IntegerField(default=0)
    course_status = models.CharField(max_length=10)

    def __str__(self):
        return self.course_id +' '+ self.course_name +' '+ self.course_semester +' '+ 'STATUS : ' + self.course_status
    
    
    