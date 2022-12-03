
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('galery/', views.galery, name='website-galery'),
    path('prenumerate/', views.prenumerate, name='website-prenumerate')
]