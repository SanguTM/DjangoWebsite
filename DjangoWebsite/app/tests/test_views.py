from django.test import SimpleTestCase, Client
from django.urls import reverse
from app.models import Post
from Users.models import Profile, User
from django.contrib.auth.models import User
import json
from django.http import HttpRequest, HttpResponse

class TestView(SimpleTestCase):
    databases = '__all__'
    def setUp(self):
        # Create some users
        self.user_1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')

        user_1 = User.objects.all().get(username='Chevy Chase')
        self.post = Post.objects.create(
            title='postas1',
            content='random post',
            author = user_1)
     
    def test_project_home_GET(self):
        client = Client()
        url = reverse('website-home')
        response = client.get(url)

        self.assertEquals(response.status_code, 200)
        #self.client.login(username='Sangu', password='123')
        print(response.template_name)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_project_postdetail_GET(self):
        client = Client()
        url = reverse('post-detail', args='1')
        response = client.get(url)

        self.assertEquals(response.status_code, 200)
        #self.client.login(username='Sangu', password='123')
        print(response.template_name)
        self.assertTemplateUsed(response, 'app/post_detail.html')

    def tearDown(self):
        # Clean up after each test
        self.user_1.delete()
        self.post.delete()

        