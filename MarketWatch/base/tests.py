from django.test import TestCase
from django.urls import reverse, resolve
from base.views import home, financial_trends, loanCalculator, profile, edit_profile, information, editInformation, loginUser, logoutUser, signup

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
