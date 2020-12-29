# users/urls.py

from django.urls import path
from . import views
from django.conf.urls import include 
from users.views import dashboard, register

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("oauth/", include("social_django.urls")),
    path("register/", views.register, name="register"),
]