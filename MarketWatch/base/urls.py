from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="home"),
    path('profile/', views.profile, name="profile"),
    path('insights/', views.insights, name="insights"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
]
