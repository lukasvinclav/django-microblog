from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.visible()


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.visible()
