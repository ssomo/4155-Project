from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Financial_Information
from .forms import CustomUserForm, FinanceForm, ProfileForm
import http.client
import json

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def market_analytics(request):
    return render(request, 'base/market_analytics.html')

def financial_trends(request):
    return render(request, 'base/financial_trends.html')

def loanCalculator(request):
    user = Financial_Information.objects.get(user=request.user)

    connection = http.client.HTTPSConnection("mortgage-monthly-payment-calculator.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "c23b5bda60msh87ee7e2a3b398f0p19db4ajsn393e1f4f609f",
        'X-RapidAPI-Host': 'mortgage-monthly-payment-calculator.p.rapidapi.com'
    }

    loanAmount = int(user.loan_amount)
    terms = user.monthly_loan_term

    connection.request("GET", f"/revotek-finance/mortgage/monthly-payment?loanAmount={loanAmount}&interestRate=0.05&terms={terms}", headers=headers)
    res = connection.getresponse()
    data = res.read()

    payment = json.loads(data.decode("utf-8"))
    amount = round(payment.get('monthlyPayment'), 2)

    context = {'user': user, 'amount': amount}

    return render(request, 'base/loan_calculator.html', context)

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

@login_required
def information(request):
    user = request.user

    try:
        info = Financial_Information.objects.get(user=request.user)
    except Financial_Information.DoesNotExist:
        info = None

    if request.method == 'POST':
        form = FinanceForm(request.POST, instance=info)
        
        if form.is_valid():
            financial_info = form.save(commit=False)
            financial_info.user = user
            financial_info.save()
            messages.success(request, 'Your financial information was successfully saved.')
            return redirect('information')
        else:
            messages.error(request, 'There are errors in your form. Please try again')
    else:
        form = FinanceForm(instance=info)

    context = {'form': form, 'user': user}
    return render(request, 'base/information.html', context)

@login_required
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