
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm,LoginForm
from django.template.loader import get_template
from django.template import Context
from .models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect



class RegisterView(FormView):
    """sign up user view"""
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('custom_auth:login')

    def form_valid(self, form):

        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)



class LoginView(FormView):


    form_class = LoginForm
    success_url = reverse_lazy('index')
    template_name = 'login.html'

    def form_valid(self, form):

        credentials = form.cleaned_data
        email = credentials['email']
        password = credentials['password']
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        if user is not None and user.password == password :
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('custom_auth:login'))