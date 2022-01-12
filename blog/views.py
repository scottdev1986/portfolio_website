from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

def blog(request, slug):
    posts = get_object_or_404(Post,slug=slug)
    recent_posts = Post.objects.all().order_by('-published_date').filter(is_published=True)[:4:1]
    comments = Comment.objects.all().order_by('-date_added').filter(post=posts.id)

    context = {
        'posts' : posts,
        'recent_posts' : recent_posts,
        'comments' : comments
    }

    return render(request, 'blog/single_post.html', context)


