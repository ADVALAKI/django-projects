from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenge = {'january': "Eat no meat for the entire month!",
                    'february': "Walk for at least 20 minutes every day!",
                    'march': "Learn Django for at least 20 minutes every day!",
                    'april': "Eat no meat for the entire month!",
                    'may': "Walk for at least 20 minutes every day!",
                    'june': "Learn Django for at least 20 minutes every day!",
                    'july': "Eat no meat for the entire month!",
                    'august': "Walk for at least 20 minutes every day!",
                    'september': "Learn Django for at least 20 minutes every day!",
                    'october': "Eat no meat for the entire month!",
                    'november': "Walk for at least 20 minutes every day!",
                    'december': "read for at least 20 minutes every day!"}

def january(request):
    return HttpResponse("Eat no meat for the entire month!")

def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")

def monthly_challenges_by_number(request, month=1):
    if month > 12:
        return HttpResponseNotFound("This month is not supported!")
    months = list(monthly_challenge.keys())
    months = months[month-1]
    return HttpResponseRedirect("/month/" + months + "/")


def monthly_challenges(request, month):
    challenge_text = monthly_challenge.get(month)
    if challenge_text:
        return HttpResponse(challenge_text)
    else:
        return HttpResponseNotFound("This month is not supported!")
