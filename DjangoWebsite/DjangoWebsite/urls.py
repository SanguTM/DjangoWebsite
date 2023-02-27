"""
Definition of urls for DjangoWebsite.
"""

from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin
from Users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from Users.views import PasswordsChangeView
from Users import views
from django.views.generic.base import TemplateView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from app.models import Post, Category
from app.sitemaps import StaticViewSitemap


#https://learndjango.com/tutorials/django-sitemap-tutorial
#https://ordinarycoders.com/blog/article/robots-text-file-django

sitemaps = {
    'post': GenericSitemap({
        'queryset': Post.objects.all(),
        'date_field': 'date_posted',
    }, priority=0.9),
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password/', PasswordsChangeView.as_view(template_name='users/change-password.html'),  name='password'),
    path('password-success/', views.password_success, name='password-success'),
    path('', include('app.urls')),
    path("robots.txt",TemplateView.as_view(template_name="app/robots.txt", content_type="text/plain")),  #add the robots.txt file
    path('sitemap.xml', sitemap,
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)