from django.urls import path,include
from . import views
from .views import User_Registretion_Form,User_profile_edit_Form,Password_Change_view,success_page
from django.contrib.auth import views as auth_view

urlpatterns = [

   path('register/',User_Registretion_Form.as_view(),name='Registretion_link'),
   path('login/',User_Registretion_Form.as_view(),name='login'),
   path('edit_user_profile/',User_profile_edit_Form.as_view(),name='edit_profile_link'),



   #path('password/',auth_view.PasswordChangeView.as_view(template_name="registration/change_passowrd.html"))

   path('password/',Password_Change_view.as_view(template_name = "registration/change_passowrd.html"),name='password_change_link'),

   path('password_reste_success/',views.success_page,name='success_page_link')


]
