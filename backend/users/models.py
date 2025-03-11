from django.contrib.auth.models import AbstractUser # Lets us to customize Django default user modle
from django.db import models # To create database tables and fields
from django.core.exceptions import ValidationError # Raise Errors when data does not meet certain rules
 
class User(AbstractUser): # A custom user model named User that extends Django's built in AbstractUser. This lets you add more fields to the default Django user
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    
    ROLE_CHOICES = [ # Choice fields (Gender and Role) These provide predefined choices for certain fields. They restrict user inputs to just the specific value (Like Female and Male)
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    
    # How you store stuffs for the infos
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    us_phone_number = models.CharField(max_length= 10, unique=True, null=False)  
    email = models.EmailField(unique=True, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    birth_date = models.DateField(null=False)
    grad_date = models.IntegerField(default=0, null=False)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default= 'user')
    created_at = models.DateTimeField(auto_now_add=True)
    major =models.CharField(max_length = 20, default= '', null=False)
    
    REQUIRED_FIELDS = ['major', 'us_phone_number', 'email', 'gender', 'birth_date',  ]
    # It controls which fields django prompts you for when creating a user via the createsuperuser
    
    def save(self, *args, **kwargs):
        self.clean() # First ensuring all validation rules are checked before savings
        super().save(*args, **kwargs) # Save method to actualy store data in the database

    def __str__(self):
        return self.username # Defines how the user instance is represented as a string. Whenever a user object is printed or shown in admin panels, it will display the username.
