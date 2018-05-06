from django.shortcuts import render, get_object_or_404, redirect, render_to_response, reverse
from django.views.generic import TemplateView, DetailView, ListView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from mysite.forms import SignupForm, LoginForm


def index(request):
    return render(request, 'include/index.html')


def login(request):
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            auth.login(request, form.cleaned_data['user'])
            if redirect_to:
                return redirect(redirect_to)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'include/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.save()
            auth.login(request, u)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'include/signup.html', {'form': form})


@login_required
def logout(request):
    redirect_to = request.GET.get('next')
    auth.logout(request)
    if redirect_to:
        return redirect(redirect_to)
    return redirect('/')

