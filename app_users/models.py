# from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=150, unique=True)  # Username field
#     password = models.CharField(max_length=128)  # Password field
#     # email = models.EmailField(unique=True)  # Email field

#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  # ชื่อผู้ใช้
    password = models.CharField(max_length=128)  # รหัสผ่าน

    def save(self, *args, **kwargs):
        # เข้ารหัสรหัสผ่านก่อนบันทึก
        if not self.pk:  # เช็คว่าผู้ใช้ใหม่หรือไม่
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


