from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import User, Employer, Job
from .forms import UserRegistrationForm
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})
