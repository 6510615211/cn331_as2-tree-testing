from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('enroll_check', views.enroll_check,name='enroll_check'),
    #path('courses',views.courses,name='courses'),

]