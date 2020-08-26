from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def home(request):

    all_posts = Post.objects.all()

    return render(request, 'index.html', {'posts': all_posts})


def post_single(request, post):

    post = get_object_or_404(Post, slug=post)

    return render(request, 'detail.html', {'post': post})
