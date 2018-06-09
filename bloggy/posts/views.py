from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .forms import CommentForm
from .models import Comment, Post


# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                body=form.cleaned_data['body'],
                created_at=datetime.now(),
                author=request.user,
                post=post
            )
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'detail.html', context)
