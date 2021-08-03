from django.urls import path
from. import views


urlpatterns = [
    #Paths Core
   
    path('',views.blog, name="blog"),
    
]
