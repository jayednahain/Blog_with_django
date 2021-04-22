from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.views.generic import DeleteView,ListView,DetailView,CreateView,UpdateView
from .models import Post,Category
from .forms import PostForm,PostFormUpdate
from django.urls import reverse_lazy,reverse
from textblob import TextBlob,Word

import random
import time

import requests


# Create your views here.
'''# function based view
def home(request):
   return render(request,'home.html')
'''

#class based view
# for class view we need change the url.py path system
class HomeView(ListView):
   model = Post
   template_name = 'home.html'
   cats = Category.objects.all()
   ordering = ['-post_date']
   #ordering = ["-id"]

   def get_context_data(self,*args,**kwargs): #helps us to grab the context data we pass in eaither thorugh view or URL
      category_menu = Category.objects.all()
      context = super(HomeView, self).get_context_data(*args,**kwargs)


      context["category_menu"]=category_menu

      return context

class Post_Cards_View(ListView):
   model = Post
   template_name = 'post_card_view.html.html'
   cats = Category.objects.all()
   ordering = ['-post_date']
   #ordering = ["-id"]

   def get_context_data(self,*args,**kwargs):
      category_menu = Category.objects.all()
      context = super(HomeView, self).get_context_data(*args,**kwargs)


      context["category_menu"]=category_menu

      return context

#def cat_manu(request):
   #categs = Category.objects.all()
   #return render(request,'home.html',{"cats":categs})

################
class PostView(DetailView):
   model = Post
   template_name = "read_post.html"

   def get_context_data(self,*args,**kwargs):
      category_menu = Category.objects.all()
      context = super(PostView, self).get_context_data(*args,**kwargs)

      #likes
      get_data = get_object_or_404(Post,id=self.kwargs['pk'])
      total_likes = get_data.likes_count() #assning the count function

      liked = False
      if get_data.likes.filter(id=self.request.user.id).exists():
         liked=True


      #sending data to front-end
      context["category_menu"]=category_menu
      context["total_likes"]=total_likes
      context["liked"]=liked



      return context

class CreatePostView(CreateView):
   model = Post
   template_name = "create_post.html"
   #fields = '__all__' #use for select all the field
   #fields = ('title','body') #selected field
   form_class = PostForm

   '''def get_context_data(self,*args,**kwargs):
      category_menu = Category.objects.all()
      context = super(CreatePostView, self).get_context_data(*args,**kwargs)
      context["category_menu"]=category_menu

      return context'''



def LikeView(request,pk):
   post = get_object_or_404(Post,id=request.POST.get('post_id'))
   #post.likes.add(request.user)
   liked =False
   if post.likes.filter(id = request.user.id).exists():
      post.likes.remove(request.user)
      liked =False
   else:
      post.likes.add(request.user)
      liked =True

   return HttpResponseRedirect(reverse('post_link',args=[str(pk)]))




class CreateCategoryView(CreateView):
   model = Category
   template_name = "create_category.html"
   fields = '__all__'

   def get_context_data(self,*args,**kwargs):
      category_menu = Category.objects.all()
      context = super(CreateCategoryView, self).get_context_data(*args,**kwargs)
      context["category_menu"]=category_menu

      return context






#defineing the category view as function
#this will get a category show the all posts which are including wtih that specific category
def CategoryView(request,cats):

   category_post = Post.objects.filter(category=cats)

   return render(request,'category_view.html',{'cats':cats,"category_post":category_post})


def CategoryListView(request):

   category_post_list = Category.objects.all()

   return render(request,'category_view_list.html',{'category_post_list':category_post_list})



class UpdatePostView(UpdateView):
   model =Post
   template_name = "update_post.html"
   # selecting the fields we want to update
   #fields = ['title','title_page','body']
   form_class = PostFormUpdate

   def get_context_data(self,*args,**kwargs):
      category_menu = Category.objects.all()
      context = super(UpdatePostView, self).get_context_data(*args,**kwargs)
      context["category_menu"]=category_menu

      return context

class DeletePostView(DeleteView):
   model = Post
   template_name = 'delete_post.html'
   success_url = reverse_lazy('home_link')

   def get_context_data(self,*args,**kwargs):
      category_menu = Category.objects.all()
      context = super(DeletePostView, self).get_context_data(*args,**kwargs)
      context["category_menu"]=category_menu

      return context



def  text_analysis(request):
   if request.method == 'POST':
      # HTML to python variable
      category_menu = Category.objects.all()


      raw_data = request.POST['sumitted_text']
      blob_ob = TextBlob(raw_data)
      text_words = blob_ob.words
      text_sentences = blob_ob.sentences
      sad_sentance = []
      happy_sentence = []
      for sentence in blob_ob.sentences:
         if sentence.sentiment.polarity < -0.1:
            sad_sentance.append(sentence)
         elif sentence.sentiment.polarity > 0.1:
            happy_sentence.append(sentence)



      return render(request, 'text_analysis.html', {"data": raw_data,

                                                    "words":text_words,
                                                    "category":category_menu,
                                                    "sentences":text_sentences,
                                                    "sad_sentence":sad_sentance,
                                                    "happy_sentence":happy_sentence

                                                    })
   else:
      raw_data ="type your post"
      return render(request, 'text_analysis.html', {"data": raw_data})






