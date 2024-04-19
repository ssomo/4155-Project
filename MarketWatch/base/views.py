from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Financial_Information
from .forms import CustomUserForm, FinanceForm, ProfileForm

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
    user = request.user
    form = ProfileForm(instance=user)
    context = {'user': user, 'form': form}

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated.')
            return redirect('profile')
        
    return render(request, 'base/edit_profile.html', context)

def information(request):
    user = Financial_Information.objects.get(user=request.user)
    form = FinanceForm(instance=user)

    if request.method == 'POST':
        form = FinanceForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your financial information was successfully saved.')
            return redirect('information')
        else:
            messages.error(request, 'There are errors in your form. Please try again')

    context = {'form': form, 'user': user}
    return render(request, 'base/information.html', context)

def editInformation(request):
    user = Financial_Information.objects.get(user=request.user)
    form = FinanceForm(instance=user)
    context = {'user': user, 'form': form}

    if request.method == 'POST':
        form = FinanceForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your financial information was successfully updated.')
            return redirect('information')
   
    return render(request, 'base/edit_information.html', context)

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