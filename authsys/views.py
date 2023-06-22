from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CustomUser
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.


class SignUpView(CreateView):
    model = CustomUser
    template_name = 'authsys/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('get_to_main')
    extra_context = {'title': 'Create your account'}

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class SignInView(LoginView):
    form_class = SignInFormSecurity
    template_name = 'authsys/login.html'
    extra_context = {'title': 'Login'}




    def get_success_url(self):
        return reverse_lazy('get_to_main')


def log(request):
    logout(request)
    return redirect('get_to_main')