from django.contrib import admin
from .models import Student, Program, Student_profile, CohortGroup

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['username', 'first_name', 'last_name', 'status']

@admin.register(Student_profile)
class profileAdmin(admin.ModelAdmin):
  list_display = ['student','date_of_birth', 'rating', 'date_join', 'address']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
  list_display = ['courses', 'grade']

@admin.register(CohortGroup)
class CohortAdmin(admin.ModelAdmin):
  list_display = ['name',  'date_join']

# admin.site.register(Student)
