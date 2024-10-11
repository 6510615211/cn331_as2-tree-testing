from django.contrib import admin
from app_courses.models import Subject
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id' ,'course_name','course_semester','course_amount','course_status']
    search_fields = ['course_id','course_name']

admin.site.register(Subject,CourseAdmin)