from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import *

class UserLogin(LoginView):
    template_name = 'users/login.html'

def create_account(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request, 'users/signup.html', {'form': form})

def homepage(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, 'Profile updated successfully!')
    
    return render(request, 'users/home.html', {'u_form': u_form, 'p_form': p_form})

class LogoutUser(LogoutView):
    template_name = 'users/login.html'