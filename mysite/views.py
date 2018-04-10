from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SubscribersForms
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

def landing(request):
    name = "Виктория"
    current_day = "26.03.2018"
    form = SubscribersForms(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        form.save()
        return HttpResponseRedirect(request.path)

    return render(request, 'landing/landing.html', locals())


def index(request):
    return render(request, 'landing/index.html', locals())


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/index/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
