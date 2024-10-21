from django.urls import path
from .views import Bloghome, Post_list,home
from .about import About_us, Contact_us


urlpatterns = [
    path('',Bloghome,name='home' ),
    path('about_us', About_us, name='aboutus'),
    path('contact_us', Contact_us, name='contactus'),
    path('post_list', Post_list, name='post'),
    path('test', home, name='test'),


]
