from django.urls.conf import path
from . import views


urlpatterns = [
    #Paths Core
    path('',views.home, name="home"),
    path('blog/',views.blog, name="blog"),
    path('sample/',views.sample, name="sample"),
    path('contact/',views.contact, name="contact"),
    
]
