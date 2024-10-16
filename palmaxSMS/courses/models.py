from django.db import models
from users.models import Teacher


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    topics = models.ForeignKey(Topic, on_delete=models.CASCADE) # Can hold a list of topics
    duration = models.DurationField()  # Store duration in a timedelta format

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Links to Teacher model in users app
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Links to Subject model
    duration = models.DurationField()  # Store duration in a timedelta format

    def __str__(self):
        return self.name