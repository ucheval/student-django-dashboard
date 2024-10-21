from django.contrib import admin
from .models import Student_profile

# Register your models here.



@admin.register(Student_profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['profile_picture', 'full_name', 'cohort', 'program', 'status', 'date_join', 'rating']