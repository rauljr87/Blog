# Vistas basadas en clases
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, PostView, Like
# class form, se los debe especificar en los modelos de PostCreateView y PostUpdateView
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    # PostForm
    form_class = PostForm
    model = Post
    # lista de campos que tiene el modelo Post para crear
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug'
    )


class PostUpdateView(UpdateView):
    # PostForm
    form_class = PostForm
    model = Post
    # lista de campos que tiene el modelo Post a actualizar
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug'
    )


class PostDeleteView(DeleteView):
    model = Post
    # redirecciona al mismo view que estamos viendo el listado de post = página principal
    success_url = '/'
