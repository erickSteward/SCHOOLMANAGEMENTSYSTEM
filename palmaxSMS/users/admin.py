from django.contrib import admin
from .models import Student, Teacher, Receptionist

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'date_of_admission', 'current_course')
    search_fields = ('first_name', 'last_name', 'username', 'national_id')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'department')
    search_fields = ('first_name', 'last_name', 'username', 'department')

@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username')
    search_fields = ('first_name', 'last_name', 'username')
