from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            messages.success(request, ('Wrong password! Please try again'))
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'index.html', {'form': form})

