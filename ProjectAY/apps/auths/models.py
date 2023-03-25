from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from students.models import Course
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
    
    

class Primary(AbstractUser):
    DEPARTMENTS = (
        ("COMPUTER SCIENCE", "COMPUTER SCIENCE"),
        ("HOSPITALITY MANAGEMENT", "HOSPITALITY MANAGEMENT"),
        ("BUSINESS ADMINISTRATION", "BUSINESS ADMINISTRATION"),
        ("STATISTICS", "STATISTICS"),
        ("OFFICE TECHNOLOGY MANAGEMENT", "OFFICE TECHNOLOGY MANAGEMENT"),
        ("BUILDING TECHNOLOGY", "BUILDING TECHNOLOGY"),
        ("MASS COMMUNICATION", "MASS COMMUNICATION"),
        ("MECHANICAL ENGINEERING", "MECHANICAL ENGINEERING"),
        ("ELECTRICAL ENGINEERING", "ELECTRICAL ENGINEERING"),
        ("POLYMER & TEXTILE", "POLYMER & TEXTILE")
        
    )
    
    GENDER = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE")
    )
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    matric_number = models.CharField(max_length=40)
    year = models.CharField(max_length=4)
    department = models.CharField(choices=DEPARTMENTS, max_length=50)
    gender = models.CharField(choices=GENDER, max_length=6)
    course = models.ManyToManyField(Course)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=["password"]
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.first_name} {self.department}"