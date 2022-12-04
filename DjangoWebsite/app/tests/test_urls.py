from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import home, PostListView, UserPostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, about, galery, prenumerate, UserPostListView
from Users.views import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('website-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_about_url_is_resolved(self):
        url = reverse('website-about')
        print(resolve(url))
        self.assertEqual(resolve(url).func, about)

    def test_galery_url_is_resolved(self):
        url = reverse('website-galery')
        print(resolve(url))
        self.assertEqual(resolve(url).func, galery)

    def test_prenumerate_url_is_resolved(self):
        url = reverse('website-prenumerate')
        print(resolve(url))
        self.assertEqual(resolve(url).func, prenumerate)

    def test_details_url_is_resolved(self):
        url = reverse('post-detail', args='1')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_create_url_is_resolved(self):
        url = reverse('post-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_update_url_is_resolved(self):
        url = reverse('post-update', args='1')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_delete_url_is_resolved(self):
        url = reverse('post-delete', args='1')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)

    def test_userposts_url_is_resolved(self):
        url = reverse('user-posts', args='1')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_passwordreset_url_is_resolved(self):
        url = reverse('password-reset')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PasswordResetView)

