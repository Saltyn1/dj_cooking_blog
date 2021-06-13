from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import User
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .forms import RegistrationForm

class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    success_message = 'Successfully registered!'

class SignInView(LoginView):
    template_name = 'account/login.html'

# class ProfileView(DetailView):
#     model = User
#     templat_name = 'account/profile.html'

def profile(request):
    return render(request, 'account/profile.html')


