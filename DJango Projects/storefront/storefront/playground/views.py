from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def playground(request):
    return HttpResponse("Hello Guys Chai pilo !!!")