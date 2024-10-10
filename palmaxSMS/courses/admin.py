from django.contrib import admin
from .models import Course, Subject, Topic, Teacher

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)
  
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'topics', 'duration')
  search_fields = ('name', 'topic',)

  
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ('name', 'teacher', 'subject', 'duration')
  search_fields = ('name', 'teacher', 'subeject', 'duration')