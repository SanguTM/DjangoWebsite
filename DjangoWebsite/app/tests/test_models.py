from django.test import SimpleTestCase, Client
from django.urls import reverse
from app.models import Post
from Users.models import Profile, User
from django.contrib.auth.models import User
import json
from django.http import HttpRequest, HttpResponse

class ModelsView(SimpleTestCase):
    databases = '__all__'

    def setUp(self):
        # Create some users
        self.user_1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')

        user_1 = User.objects.all().get(username='Chevy Chase')
        self.post = Post.objects.create(
            title='postas1',
            content='random post',
            author = user_1)

    def test_user_is_assigned(self):
        user_1 = User.objects.all().get(username='Chevy Chase')
        self.assertEquals(user_1.username, 'Chevy Chase')

    def test_post_is_assigned(self):
        user_1 = User.objects.all().get(username='Chevy Chase')
        post = Post.objects.get(title='postas1')
        self.assertEquals(post.title, 'postas1')
      
    def tearDown(self):
        # Clean up after each test
        self.user_1.delete()
        self.post.delete()
