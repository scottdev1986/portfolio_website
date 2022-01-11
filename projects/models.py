from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    project_url = models.URLField(max_length=200)
    github_url = models.URLField(max_length=200)
    body = models.TextField()
    photo_1 = models.ImageField(upload_to='photos/projects/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/projects/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/projects/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
