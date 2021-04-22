from django.urls import path,include
from . import views
from .views import User_Registretion_Form

urlpatterns = [

   path('register/',User_Registretion_Form.as_view(),name='Registretion_link'),
   path('login/',User_Registretion_Form.as_view(),name='login')

]
