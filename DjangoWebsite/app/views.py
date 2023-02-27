"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.http import HttpResponse
from .models import Post, Comment, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm, PostForm

def home(request):
    context = {
            'posts':Post.objects.all()
        }
    return render(request, 'app/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class UserPostListView(ListView):
    model = Post
    template_name = 'app/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserPostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    #fields isvardinami tik tuo atveju, jei nera naudoja custom forma is views.py, kitu atveju form_class
    #fields =['title', 'category', 'content']
    #template_name = 'app/post_form.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostCreateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    #fields =['title', 'content']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDeleteView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'app/about.html', {'title': 'About'})

def gallery(request):
    return render(request, 'app/gallery.html')

def prenumerate(request):
     return render(request, 'app/prenumerate.html')


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'app/add_comment.html'
    form_class = CommentForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CommentCreateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class CategoryView(ListView):
    model = Post
    template_name = 'app/categories.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        c = self.kwargs.get('cats')
        curr_cat = Category.objects.get(code=c)
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["curr_cat"] = curr_cat
        return context

    def get_queryset(self):
        cats = get_object_or_404(Category, code=self.kwargs.get('cats'))
        return Post.objects.filter(category=cats).order_by('-date_posted')

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields ='__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CategoryCreateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)