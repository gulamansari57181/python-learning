from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Welcome to Django Project")

def home(request):
    return HttpResponse("Hello Welcome to Learning Home")

def aboutUs(request):
    return HttpResponse("To kaise hai aap log ?")