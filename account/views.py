from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import MyLoginForm, MyRegisterForm


def mylogin(request):
    form = MyLoginForm()
    if request.user.is_authenticated:
        messages.error(request, 'eror')
        return redirect('karzinka:home')
    if request.method == "POST":
        form = MyLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'login')
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('karzinka:home')
    ctx = {
        'form': form
    }
    return render(request, 'account/login.html', ctx)


def mylogout(request):
    if not request.user.is_authenticated:
        messages.error(request, 'eror')
        return redirect('karzinka:home')
    if request.method == "POST":
        logout(request)
        messages.error(request, 'logout')
        return redirect('account:login')
    return render(request, 'account/logout.html')


def myregister(request):
    if request.user.is_authenticated:
        messages.error(request, 'eror')
        return redirect('karzinka:home')
    form = MyRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'register')
        return redirect('account:login')
    ctx = {
        'form': form
    }
    return render(request, 'account/register.html', ctx)