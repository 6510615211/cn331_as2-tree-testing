from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  
    password = models.CharField(max_length=128) 

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


