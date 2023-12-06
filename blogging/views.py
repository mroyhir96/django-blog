from django.shortcuts import render
from django.http import Http404
from django.views import View
#from django.views.generic import ListView, DetailView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blogging.models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    context_object_name = 'posts'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
    queryset = Post.objects.exclude(published_date__exact=None)
