from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login
from . import forms, models


def default(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            # auto-login user
            login(request.user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'review/login.html', {'form': form})

def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    context = {'tickets': tickets, 'reviews': reviews}
    return render(request, 'review/home.html', context)

def signup(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-loging user
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'review/signup.html', context={'form': form})

def posts(request):
    return render(request, 'review/posts.html')

def subs(request):
    return render(request, 'review/subs.html')

def create_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')

    context = {'ticket_form': ticket_form}
    return render(request, 'review/create_ticket.html', context)

def create_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {'ticket_form': ticket_form, 'review_form': review_form}
    return render(request, 'review/create_review.html', context)