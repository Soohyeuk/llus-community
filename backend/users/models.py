from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class User(AbstractUser):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    
    username = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=100)
    us_phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    school = models.CharField(max_length=255)
    grad_date = models.IntegerField()
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    REQUIRED_FIELDS = ['username', 'major', 'us_phone_number', 'gender', 'birth_date', 'school', 'generation', 'role']

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
