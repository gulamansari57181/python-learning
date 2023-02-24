from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect


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
def monthly_challenge_by_number(request,month):
    # To redirect 1- january, 2-febuary
    months_list=list(challenge_text.keys())
    redirect_month=months_list[month-1]
    
    return HttpResponseRedirect("/challenge/" + redirect_month)
    

# Create a view for dynamic route
def monthly_challenge(request, month):
    try:
        challenge=challenge_text[month]
        return HttpResponse(f"<h1>Challenge : {challenge} </h1>") 
    except:
        return HttpResponseNotFound("Mentioned month is not a valid month !!")
        
    