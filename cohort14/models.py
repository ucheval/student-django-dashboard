from django.db import models

# Create your models here.


class Student_profile(models.Model):
  profile_picture = models.ImageField(upload_to= 'student_profile')
  full_name = models.CharField(max_length=200)
  cohort = models.CharField(max_length=50)
  program = models.CharField(max_length=200)
  date_join = models.DateTimeField(auto_now_add=True)
  rating = models.FloatField(default=0.0)
  status = models.BooleanField(default= True)
  # actions = [
  #       (1, 'Online Exam'),
  #       (0, 'Class Exam'),
  #       (-1, 'Missed Exam'),
  #   ]
  
  def str(self):
    return f"{self.full_name}"