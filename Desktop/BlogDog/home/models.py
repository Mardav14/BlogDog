from django.db import models

# Create your models here.
class Blog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    content = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'static/post/')
    date = models.DateTimeField(auto_now_add = True, null = True)

class Comment(models.Model):
    comment = models.TextField()
