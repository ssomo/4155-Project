from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from base.views import home, financial_trends, loanCalculator, profile, edit_profile, information, editInformation, loginUser, logoutUser, signup
from base.models import Financial_Information, Notification
from django.contrib.auth.models import User
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
        
# Views Tests
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.financial_trends_url = reverse('financial_trends')
        self.profile_url = reverse('profile')
        self.information_url = reverse('information')
        self.edit_information_url = reverse('edit_information')
        self.login_user_url = reverse('login')
        self.logout_user_url = reverse('home')
        self.signup_url = reverse('signup')
        

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')

    def test_financial_trends_GET(self):
        response = self.client.get(self.financial_trends_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/financial_trends.html')
    
    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        if(self.assertEquals(response.status_code, 302)):
            self.assertTemplateUsed(response, 'base/profile.html')
    
    def test_information_GET(self):
        response = self.client.get(self.information_url)
        self.assertEquals(response.status_code, 302)
    
    def test_edit_formation_GET(self):
        response = self.client.get(self.edit_information_url)
        self.assertEquals(response.status_code, 302)

    def test_loginUser_GET(self):
        response = self.client.get(self.login_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login.html')

    def test_logoutUser_GET(self):
        response = self.client.get(self.logout_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')
    
    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/signup.html')

# Model Tests
class TestModels(TestCase):
    def setUp(self):
        self.user1 = Financial_Information.objects.create(
            user = User(Financial_Information.user_id),
            state = 'NC', 
            income_level = 32500,
            credit_score = 550,
            loan_amount = 300000,
            monthly_loan_term = 360,
            down_payment = 3000,
            property_value = 250000
        )
        Financial_Information.save()
        self.notification1 = Notification.objects.create(
            user = User(Notification.user_id),
            timestamp = 1337453263.939,
            is_read = True,
            message = 'Sample Text'
        )
        
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
