from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_analytics, name="market_analytics"),
    path('financial_trends/', views.financial_trends, name="financial_trends"),
    path('reports/', views.reports, name="reports"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('login/', views.loginUser, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logoutUser, name="logout")
]
