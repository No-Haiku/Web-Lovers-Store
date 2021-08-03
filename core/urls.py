from django.urls.conf import path
from . import views


urlpatterns = [
    #Paths Core
    path('',views.home, name="home"),
    
    path('sample/',views.sample, name="sample"),
    path('contact/',views.contact, name="contact"),
    
]
