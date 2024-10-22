from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses, name='courses'),
    path('enroll_check', views.enroll_check,name='enroll_check'),
]