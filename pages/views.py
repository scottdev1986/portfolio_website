from django.shortcuts import render
from blog.models import Post
from projects.models import Project

def index(request):
    posts = Post.objects.order_by('-published_date').filter(is_published=True)
    projects = Project.objects.order_by('-published_date').filter(is_published=True)

    context = {
        'posts' : posts,
        'projects' : projects
    }

    return render(request, 'pages/index.html', context)
