from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import Post, Comment

def comment(request):
    if request.method == 'POST':
        post = request.POST['post_id']
        slug = request.POST['slug_id']
        name = request.POST['user_name']
        email = request.POST['user_email']
        body = request.POST['comment_body']
    
    post_instance = get_object_or_404(Post, id=post)
    
    comment = Comment(post=post_instance ,name=name, email=email, body=body)

    comment.save()

    return redirect('/blog/'+slug)
