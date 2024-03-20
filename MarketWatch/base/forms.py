from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Financial_Information

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Financial_Information
        fields = ['state', 'income_level', 'credit_score', 'debt_ratio', 
                  'loan_amount', 'loan_term', 'down_payment', 'property_value']