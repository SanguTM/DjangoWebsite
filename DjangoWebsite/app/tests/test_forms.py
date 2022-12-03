from django.test import SimpleTestCase, Client
from django.urls import reverse
from app.models import Post
from Users.models import Profile, User
from django.contrib.auth.models import User
import json
from django.http import HttpRequest, HttpResponse
from Users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

class ModelsView(SimpleTestCase):
    databases = '__all__'

    def test_UserRegisterForm_for_valid_data(self):
        form = UserRegisterForm(data={'username': 'testas', 'email':'pastas@pastas.lt', 'password1':'mnvc2231', 'password2':'mnvc2231'})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_UserUpdateForm_for_valid_data(self):
        form = UserUpdateForm(data={'username': 'testas', 'email':'pastas@pastas.lt'})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_ProfileUpdateForm_for_valid_data(self):
        form = ProfileUpdateForm(data={'image': ''})
        print(form.errors)
        self.assertTrue(form.is_valid())
