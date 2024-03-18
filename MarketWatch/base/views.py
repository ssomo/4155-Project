from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def market_analytics(request):
    return render(request, 'base/market_analytics.html')

def financial_trends(request):
    return render(request, 'base/financial_trends.html')

def reports(request):
    return render(request, 'base/reports.html')

def profile(request):
    return render(request, 'base/profile.html')

def edit_profile(request):
    return render(request, 'base/edit_profile.html')

def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/signup.html')