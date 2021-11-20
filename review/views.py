from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login
from. import forms


def default(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-loging user
            login(request.user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'review/login.html', {'form': form})

def home(request):
    return render(request, 'review/home.html')

def signup(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-loging user
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'review/signup.html',
                  context={'form': form})