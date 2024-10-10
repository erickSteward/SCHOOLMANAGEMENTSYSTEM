from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Consider using Django's built-in authentication
    date_of_admission = models.DateField()
    current_course = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Consider using Django's built-in authentication
    department = models.CharField(max_length=100)
    subjects_teaching = models.TextField()  # Use TextField to handle multiple subjects

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Receptionist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Consider using Django's built-in authentication

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

