# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
            if user is not None:
                login(request, user)
                return redirect("profile")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})

@login_required
def profile_view(request):
    return render(request, "users/profile.html")

def logout_view(request):
    logout(request)
    return redirect("login")
