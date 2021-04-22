from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SingUpForm(UserCreationForm):


   '''first_name = forms.CharField(max_length=100)
   last_name = forms.CharField(max_length=100)'''

   email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
   first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
   last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))


   class Meta:
      model = User
      fields = ('username','first_name','last_name','email','password1','password2')


   #for appling username and password we need to define another methods

   def __init__(self,*args,**kwargs):
      super(SingUpForm,self).__init__(*args,**kwargs)

      classes={
         'class':'form-control'
      }

      '''self.fields['username'].widget.attrs['class']='form-control'
      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['class'] = 'form-control'''

      select_fields = ['username','password1','password2']

      for value in select_fields:
         self.fields[value].widget.attrs['class'] = 'form-control'
         self.fields[value].widget.attrs['placeholder'] = str(value)




class Edit_Profile_Form(UserChangeForm):

   labels_fields = ['username', 'first_name', 'last_name', 'email','last_login','is_super','is_staff','is_active','date_joined']


   email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
   first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
   last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

   username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


   last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


   is_super = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
   is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
   is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
   date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email','last_login','is_super','is_staff','is_active','date_joined','password']



class PasswordChangingForm(PasswordChangeForm):

   old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
   new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
   new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))


   class Meta:
      model = User
      fields = ('old_password','new_password1','new_password2')