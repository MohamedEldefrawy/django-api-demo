from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AccountForm (UserCreationForm):    
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')