from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Financial_Information
from .forms import CustomUserForm, FinanceForm
import matplotlib.pyplot as plt

# Create your views here.
def market_analytics(request):
    return render(request, 'base/market_analytics.html')

def financial_trends(request):
    return render(request, 'base/financial_trends.html')

def reports(request):
    return render(request, 'base/reports.html')

def loanCalculator(request):
    return render(request, 'base/loan_calculator.html')

def profile(request):
    if request.user.is_authenticated:
        profile = User.objects.get(username=request.user.username)
        context = {'profile': profile}
        return render(request, 'base/profile.html', context)
    else:
        return redirect('market_analytics')

def edit_profile(request):
    return render(request, 'base/edit_profile.html')

def information(request):
    #Checks if the user's financial information exists
    try:
        user_info = Financial_Information.objects.get(user=request.user)
    except:
        user_info = None

    form = FinanceForm()

    if request.method == 'POST':
        if user_info:
            #Updates the financial information if it exists
            form = FinanceForm(request.POST, instance=user_info)
        else:
            #Creates a new instance if it doesn't exist
            form = FinanceForm(request.POST)
        
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            messages.success(request, 'Your financial information was successfully saved.')
            return redirect('information')
        else:
            messages.error(request, 'There are errors in your form. Please try again')
    
    else: 
        form = FinanceForm(instance=user_info)

    return render(request, 'base/information.html', {'form': form, 'user_info': user_info})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('market_analytics')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'This user does not exist.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('market_analytics')
        else:
            messages.error(request, 'Username or Password is incorrect. Please try again.')

    return render(request, 'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect('market_analytics')

def signup(request):
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('information')
        else:
            messages.error(request, 'There seems to be an issue registering this user.')

    return render(request, 'base/signup.html', {'form': form})