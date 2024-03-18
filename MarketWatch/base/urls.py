from django.urls import path
from . import views

urlpatters = [
    path('', views.dashboard, name="home"),
    path('profile/', views.profile, name="profile"),
]
