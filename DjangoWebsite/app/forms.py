from django import forms
from django.contrib.auth.forms import AuthenticationForm
from ckeditor.fields import RichTextField
from .models import Post, Comment

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
