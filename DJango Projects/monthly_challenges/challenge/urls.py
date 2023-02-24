# Importing path 
from django.urls import path
# importing views of this dircetory
from . import views

urlpatterns = [
    # part() accepts two parameters 1)String that is url we want to support 
    # 2) corresponding views for that we have to import views.py file
    # path("january",views.index),
    # path("febuary",views.febuary),
    # To handle any string url passed. we will use place holder syntax
    
    path("<month>",views.monthly_challenge)
]
