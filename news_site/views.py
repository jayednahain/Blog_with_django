from django.shortcuts import render

# Create your views here.


def home_view(request):
   return render(request,'news_home_page.html')

