from django import forms
from .models import Post,Category

#adding category manually
#but we want to
#choices = [('coding','coding'),('sports','sports'),('entertainment',	'entertainment')]

# call it from our database
choices=Category.objects.all().values_list('name','name')

choices_list = []

for items in choices:
   choices_list.append(items)

#class for posting our "posts"
class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ('title','title_page','author','category','body','snippet','headr_images')


      title_style ={
         'class': 'form-control',
         'placeholder': "Type title",

      }
      title_page_style ={
         'class': 'form-control',
         'placeholder': "Type Title Page"
      }
      author_style ={
         'class': 'form-control',
         'value':'',
         'id':'author_filed',
         'type':'hidden'

      }

      body_style={
         'class': 'form-control',
         'placeholder': "type here full post.."
      }

      category_style={
         'class': 'form-control',
         'placeholder': "Select category"
      }
      snippet_style = {
         'class': 'form-control',
         'placeholder': "write sort snippet of your post !"
      }

      widgets={
         'title':forms.TextInput(attrs=title_style),
         'title_page':forms.TextInput(attrs=title_page_style),
         'author': forms.TextInput(attrs=author_style),
         #'author':forms.Select(attrs=author_style),
         'category': forms.Select(choices=choices_list,attrs=category_style),
         'body':forms.Textarea(attrs=body_style),
         'snippet': forms.Textarea(attrs=snippet_style)
      }



class PostFormUpdate(forms.ModelForm):
   class Meta:
      model = Post
      fields = ('title','title_page','body','snippet')


      title_style ={
         'class': 'form-control'
      }
      title_page_style ={
         'class': 'form-control'
      }

      body_style={
         'class': 'form-control'
      }

      snippet_style = {
         'class': 'form-control',
         'placeholder': "write sort snippet of your post !"
      }

      widgets={
         'title':forms.TextInput(attrs=title_style),
         'title_page':forms.TextInput(attrs=title_page_style),
         'body':forms.Textarea(attrs=body_style),
         'snippet': forms.Textarea(attrs=snippet_style)
      }