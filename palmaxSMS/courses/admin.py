from django.contrib import admin
from .models import Course, Subject
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'subject', 'duration')
    search_fields = ('name', 'teacher__first_name', 'teacher__last_name', 'subject__name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration')
    search_fields = ('name',)

