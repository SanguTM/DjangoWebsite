from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Comment, Category
from django.db.utils import OperationalError

choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)
    
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
        fields = ('title','category','content')
        
        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-select'})
            }
            

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

