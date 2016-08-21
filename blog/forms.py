from django import forms
from .models import Post
from django.contrib.auth.models import User
from blog.models import UserProfile



class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text','picture')

class UserForm(forms.ModelForm):
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
            'password': forms.PasswordInput(),
        }

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('name', 'contactNo', 'address', 'bio')
