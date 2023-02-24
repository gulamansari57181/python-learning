from django.shortcuts import render
from django.http import HttpResponse


# To create month: challenge map

challenge_text={
    "january":"Learn django everyday for 30 minutes.",
    "febuary":"Do running for 1 hour.",
    "march":"Learn DSA fundamentals.",
    "april":"Learn Advance concepts of DSA.",
    "may":"Solve  2 leetcode problems daily.",
    "june":"Learn swimming.",
    "july":"Learn React.js for frontend development.",
    "august":"Make web dev projects.",
    "september":"Go for holiday trip.",
    "october":"Eat vegetable only for a month.",
    "november":"Visit NGo and help the needy people.",
    "december":"Party day in and day out !!!"
    
}

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello How you doing ??????</h1>")

# Create a view for febuary
def monthly_challenge(request, month):
    
    challenge=challenge_text.get(month)
    return HttpResponse(f"<h1>Challenge : {challenge} </h1>") 