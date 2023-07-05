from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import User, Employer, Job
from .forms import UserRegistrationForm, EmployerRegistrationForm, JobCreationForm

# Create your views here.

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('dashboard')
        else:
            form = UserRegistrationForm()
            return render(request, 'user_registration.html', {'form': form})
