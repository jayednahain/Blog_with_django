from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SingUpForm

# Create your views here.

class User_Registretion_Form(generic.CreateView):
   form_class = SingUpForm
   template_name = "registration/registration.html"
   success_url = reverse_lazy('login')