from django.shortcuts import render, redirect
from authentication import forms 
from . import models
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from .forms import UploadProfilePhotoForm

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('login')

def login_view(request):
    form = forms.LoginForm()
    message = ''
    if request.method =='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],

            )
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = 'Identifiants invalides.'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    return render(request, 'authentication/signup.html', context={'form': form} )  

def photo_upload(request):
    form = forms.UploadProfilePhotoForm()
    if request.method == 'POST':
        form = UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UploadProfilePhotoForm(instance=request.user)
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})

