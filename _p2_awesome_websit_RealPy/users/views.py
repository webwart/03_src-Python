# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm

# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html")

# def dashboard(request):
#     return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",    #changed from users/register.html to register.html 
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))