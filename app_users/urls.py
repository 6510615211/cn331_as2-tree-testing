from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # ใช้งาน URL ที่ Django เตรียมไว้สำหรับการจัดการระบบบัญชีผู้ใช้
]
