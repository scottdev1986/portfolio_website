from django import forms
from django.core import paginator
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.models import Post
from projects.models import Project
from contacts.forms import ContactForm

def index(request):
    posts = Post.objects.order_by('-published_date').filter(is_published=True)
    projects = Project.objects.order_by('-published_date').filter(is_published=True)
    form = ContactForm
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'posts' : paged_listings,
        'projects' : projects,
        'form' : form
    }

    return render(request, 'pages/index.html', context)
