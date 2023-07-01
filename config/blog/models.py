from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return('home')
STATUS_CHOICES =(
    ('draft','draft'),
    ('published','published')
)

class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    body = models.TextField()
    slug = models.SlugField(unique_for_date='pub_date')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    enable_comments = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default = 'draft')
    tags = TaggableManager(related_name="tags")

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self,):
        return reverse("detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    author = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)