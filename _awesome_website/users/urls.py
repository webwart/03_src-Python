# users/urls.py

from django.urls import path
from . import views
from django.conf.urls import include 

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
]