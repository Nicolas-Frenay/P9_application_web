from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)


class ReviewForm(forms.ModelForm):
    post_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Review
        # TODO ajouter titre et auteur au ticket ?
        fields=['rating', 'headline', 'body']


class TicketForm(forms.ModelForm):
    post_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


# """
# créer un formulaire custom sans modelform?
# ou pas de formulaire du tout ?
# """
#
# class FollowForm(forms.ModelForm):
#     users = User.objects.all()
#     class Meta:
#         model = models.UserFollows
#         fields= ['followed_user']
