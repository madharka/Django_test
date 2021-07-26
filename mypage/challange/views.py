from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
monthly_challenges = {
    "january": "january",
    "february": "february",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": "december"
}

def main_page(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for m in months:
        month_path = reverse("month_challenge", args=[m])
        list_items += f"<li><a href=\"{month_path}\">{m}</a></li>" 
    return HttpResponse(f"<ul >{list_items}</ul>")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("404")
    redirect_month = months[month-1]
    return HttpResponseRedirect(redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("404")