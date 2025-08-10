from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('dashboard:index')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account created successfully. Please login.")
            return redirect('login')
    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')
