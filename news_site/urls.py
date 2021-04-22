from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home_view,name='news_home_link')


]
