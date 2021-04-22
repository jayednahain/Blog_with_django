from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SingUpForm , PasswordChangingForm,Edit_Profile_Form
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView #for showing the profile page
from Django_blog.models import Profile

# Create your views here.

class User_Registretion_Form(generic.CreateView):
   form_class = SingUpForm
   template_name = "registration/registration.html"

   #after regestration it will go for log in page
   success_url = reverse_lazy('login')




class User_profile_edit_Form(generic.UpdateView):
   form_class = Edit_Profile_Form
   template_name = "registration/edit_profile.html"

   #after regestration it will go for log in page
   success_url = reverse_lazy('home_link')

   #creating a function for sending current user data for editing !

   def get_object(self):
      return self.request.user

class Password_Change_view(PasswordChangeView):
   #from_class = PasswordChangingForm
   form_class = PasswordChangingForm
   template_name = "registration/change_passowrd.html"
   success_url = reverse_lazy('success_page_link')


def success_page(request):

   return render(request,'registration/success_page.html')
