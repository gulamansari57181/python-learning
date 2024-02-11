from django.urls import path    
from .import views

urlpatterns=[
    path("playground/",views.playground),
    path("playground2/",views.playground2),
    
]