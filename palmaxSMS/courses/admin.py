from django.contrib import admin
from .models import Course, Subject, Topic, Teacher

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)
  
