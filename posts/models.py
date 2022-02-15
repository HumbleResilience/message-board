from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model): #creating category Posts and fields in admin panel
    title = models.CharField(max_length = 256) 
    body = models.TextField()


    def __str__(self): #show titles in Posts
        return self.title          

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])