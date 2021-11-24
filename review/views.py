from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from itertools import chain
from . import forms, models


def default(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'review/login.html', {'form': form})


@login_required
def home(request):
    # tickets = models.Ticket.objects.all()
    # reviews = models.Review.objects.all()
    # tickets_and_reviews = sorted(chain(tickets, reviews),
    #                              key=lambda element: element.time_created,
    #                              reverse=True)
    # context = {'instances': tickets_and_reviews}

    own_tickets = models.Ticket.objects.filter(user=request.user)
    follow_tickets = models.Ticket.objects.filter(
        user__in=models.UserFollows.objects.filter(
            user=request.user).values_list('followed_user'))

    own_reviews = models.Review.objects.filter(user=request.user)
    follow_reviews = models.Review.objects.filter(
        user__in=models.UserFollows.objects.filter(
            user=request.user).values_list('followed_user'))

    other_reviews = models.Review.objects.filter(ticket__user=request.user)

    tickets_and_reviews = sorted(
        chain(own_tickets, follow_tickets, own_reviews, follow_reviews,
              other_reviews), key=lambda element: element.time_created,
        reverse=True)

    context = {'instances': tickets_and_reviews}

    # main = User.objects.get(id=request.user.id)
    # followed = main.following.all()
    # context = {'follow': followed}
    return render(request, 'review/home.html', context)


def signup(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-loging user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    context = {'form': form}

    return render(request, 'review/signup.html', context)


@login_required
def posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    tickets_and_reviews = sorted(chain(tickets, reviews),
                                 key=lambda element: element.time_created,
                                 reverse=True)
    context = {'instances': tickets_and_reviews}
    return render(request, 'review/posts.html', context)


@login_required
def subs(request):
    context = {}
    main_user = models.UserFollows()

    if models.UserFollows.objects.filter(user=request.user):
        context['followed'] = models.UserFollows.objects.filter(
            user=request.user)

    if models.UserFollows.objects.filter(followed_user=request.user):
        context['following'] = models.UserFollows.objects.filter(
            followed_user=request.user)

    if request.method == 'POST':
        searched_user = request.POST.get('username')
        if User.objects.get(username=searched_user):
            followed_user = User.objects.get(username=searched_user)
            main_user.followed_user = followed_user
            main_user.user = request.user
            main_user.save()
        else:
            context['error'] = 'Aucun utilisateurs trouvé !'
        return redirect('subs')

    return render(request, 'review/subs.html', context)


@login_required
def delete_sub(request, sub_id):
    sub = models.UserFollows.objects.get(id=sub_id)
    sub.delete()
    return redirect('subs')


@login_required
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


@login_required
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


@login_required
def ticket_response(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            ticket.reviewed = True
            ticket.save()
            review.save()
        return redirect('home')
    context = {'ticket': ticket, 'review_form': review_form}
    return render(request, 'review/ticket_response.html', context)
