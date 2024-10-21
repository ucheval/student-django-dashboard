from django.urls import path
from .views import cohortpage, aboutpage

urlpatterns = [
    path('',cohortpage,name='homepage' ),
    path('aboutpage/',aboutpage, name='aboutpage')
    

]