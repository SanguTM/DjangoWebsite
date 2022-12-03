from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(
        max_length=100,
        null=True
    )
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
