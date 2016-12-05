from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    me = User.objects.get(username='aaron')
    posts = Post.objects.filter(author=me)
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
