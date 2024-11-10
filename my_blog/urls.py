from django.urls import path 
#from my_blog import views
from  .import views
urlpattern=[path("blog",views.home)]