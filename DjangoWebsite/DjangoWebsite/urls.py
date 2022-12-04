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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password/', PasswordsChangeView.as_view(template_name='users/change-password.html'),  name='password'),
    path('password-success/', views.password_success, name='password-success'),
    path('', include('app.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)