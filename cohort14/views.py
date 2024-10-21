from django.shortcuts import render

# Create your views here.

def cohortpage(request):
 return render(request,'student/index.html')

def aboutpage(request):
 return render(request,'student/about.html')
