from django.db import models
import datetime as dt
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    caption = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/')

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()
        return posts
