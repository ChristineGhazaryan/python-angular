from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
import re


class RegistrationForm(UserCreationForm):
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name:
            raise forms.ValidationError("This field is required.")
        if not re.match("^[a-zA-Z]+.*", first_name):
            raise forms.ValidationError('This field must start with an alphabet character (alpha).')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name:
            raise forms.ValidationError("This field is required.")
        if not re.match("^[a-zA-Z]+.*", last_name):
            raise forms.ValidationError('This field must start with an alphabet character (alpha).')
        return last_name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError("This field is required.")
        return email

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'status']
