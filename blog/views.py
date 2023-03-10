# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# CBV 형태 코드
class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post


# FBV 형태 코드
"""
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
"""

"""
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
        }
    )
"""