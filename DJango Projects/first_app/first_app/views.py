from django.http import HttpResponse
from django.shortcuts import render

# to deal with date

import datetime

def index(request):
    date = datetime.date.today()
    # return HttpResponse("Hello Welcome to Django Project " + str(date))
    return render(request,"index.html",{})

# def home(request):
#     return HttpResponse("Hello Welcome to Learning Home")

def aboutUs(request):
    return render(request,"about.html",{})