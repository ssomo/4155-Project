from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return HttpResponse('Dashboard')

def profile(request):
    return HttpResponse('Profile')