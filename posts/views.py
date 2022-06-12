# Vistas basadas en clases
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, PostView, Like


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    # lista de campos que tiene el modelo Post
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug'
    )


class PostDeleteView(DeleteView):
    model = Post
