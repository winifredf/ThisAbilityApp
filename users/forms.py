from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Employer, Job

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'address', 'gender', 'phone', 'email', 'password', 'abilities']