from django.urls import path ,include
from . import views


urlpatterns = [
    path('login',include('django.contrib.auth.urls'))
]