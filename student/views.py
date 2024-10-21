from django.shortcuts import render
from .models import Student


# Create your views here.

def home(request):
    # return HttpResponse('welcome to my come')
    students = Student.objects.all()
    

    return render(request, "student/index.html", {
        'students': students
    })


def about_student(request):
    
    return render(request, "student/about.html")