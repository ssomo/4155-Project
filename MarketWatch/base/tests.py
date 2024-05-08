from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from base.views import home, financial_trends, loanCalculator, profile, edit_profile, information, editInformation, loginUser, logoutUser, signup
from base.forms import CustomUserForm, FinanceForm, ProfileForm

# URL Tests
class TestUrls(TestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)
    
    def test_financial_trends_is_resolved(self):
        url = reverse('financial_trends')
        print(resolve(url))
        self.assertEqual(resolve(url).func, financial_trends)
    
    def test_profile_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEqual(resolve(url).func, profile)
    
    def test_edit_profile_is_resolved(self):
        url = reverse('edit_profile')
        print(resolve(url))
        self.assertEqual(resolve(url).func, edit_profile)
    
    def test_information_is_resolved(self):
        url = reverse('information')
        print(resolve(url))
        self.assertEqual(resolve(url).func, information)
    
    def test_editInformation_is_resolved(self):
        url = reverse('edit_information')
        print(resolve(url))
        self.assertEqual(resolve(url).func, editInformation)

    def test_loanCalculator_is_resolved(self):
        url = reverse('loan_calculator')
        print(resolve(url))
        self.assertEqual(resolve(url).func, loanCalculator)
    
    def test_loginUser_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEqual(resolve(url).func, loginUser)
    
    def test_signup_is_resolved(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEqual(resolve(url).func, signup)
    
    def test_logoutUser_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEqual(resolve(url).func, logoutUser)

# Form Tests
class TestForms(SimpleTestCase):
    databases = '__all__'
    def test_custom_user_form_valid_data(self):
        form = CustomUserForm(data={
            'first_name:' : 'Jenny',
            'last_name' : 'Williams',
            'username' : 'jwilliams1',
            'password1' : 'blueyankee22!',
            'password2' : 'blueyankee22!'
        })

        self.assertTrue(form.is_valid())

    def test_custom_user_form_no_data(self):
        form = CustomUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_finance_form_valid_data(self):
        form = FinanceForm(data={
            'state' : 'NC',
            'income_level' : 32500,
            'credit_score' : 550,
            'loan_amount' : 300000,
            'monthly_loan_term' : 360,
            'down_payment' : 3000,
            'property_value' : 250000
        })

        self.assertTrue(form.is_valid())

    def test_finance_form_no_data(self):
        form = FinanceForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)

    def test_profile_form_valid_data(self):
        form = ProfileForm(data={
            'first_name' : 'Jenny',
            'last_name' : 'Williams',
            'username' : 'jwilliams1',
            'password' : 'blueyankee22!'
        })

        self.assertTrue(form.is_valid())
    
    def test_profile_form_no_data(self):
        form = ProfileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
