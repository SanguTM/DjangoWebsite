from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='website-home'),
    path('about/', views.about, name='website-about'),
    path('galery/', views.galery, name='website-galery'),
    path('prenumerate/', views.prenumerate, name='website-prenumerate'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='post-comment'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('_user/<str:username>', UserPostListView.as_view(), name='user-posts')
]