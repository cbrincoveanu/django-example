from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Currency

def index_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'accounts/landing.html')

@login_required
def assets_view(request):
    assets = {i.currency: i.amount for i in request.user.profile.user_assets.all()}
    currencies = Currency.objects.all()
    for currency in currencies:
        if currency not in assets:
            assets[currency] = 0
    return render(request, 'accounts/assets.html', {'assets': assets})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
