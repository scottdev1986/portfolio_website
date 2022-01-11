from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return '%s %s' % (self.post.title, self.name)


