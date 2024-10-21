from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Bloghome(request):
    # return HttpResponse('welcome to my come')
    return render(request, "blog/index.html")

def home (request):
    return HttpResponse('testing')   



def Post_list(request):
    return render(request, "blog/post.html")
