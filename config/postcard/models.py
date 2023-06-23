from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.contrib.auth import get_user_model
import random
import geocoder
# Create your models here.

Token ='pk.eyJ1IjoiaWVueWVuZSIsImEiOiJjbDVwYzV3bW0wcmp6M2lvZWRmamN4cnV3In0.G3yaMn224wCZg4kS1CMbnQ'

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    image = models.ImageField(upload_to='photos')
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    location = models.CharField(max_length=200, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title + "-" + str(random.randint(10000,99999)))
        g =geocoder.mapbox(self.location,key=Token)
        g = g.latlng
        self.lat = g[0]
        self.lon = g[1]
        super(Post,self).save(*args,**kwargs)