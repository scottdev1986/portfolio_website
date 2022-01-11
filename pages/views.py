from django import forms
from django.shortcuts import render
from blog.models import Post
from projects.models import Project
from contacts.forms import ContactForm

def index(request):
    posts = Post.objects.order_by('-published_date').filter(is_published=True)
    projects = Project.objects.order_by('-published_date').filter(is_published=True)
    form = ContactForm

    context = {
        'posts' : posts,
        'projects' : projects,
        'form' : form
    }

    return render(request, 'pages/index.html', context)
