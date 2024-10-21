from django.urls import path
from .views import home, about_student

urlpatterns = [
    path('',home,name='studenthome' ),
    path('studentabout/',about_student, name='studentabout')
    

]