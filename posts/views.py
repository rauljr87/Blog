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
    success_url = '/'
    # lista de campos que tiene el modelo Post para crear
    # al modificar post_form {{ form_type }}, pide eliminar los campos
    # fields = (
    #    'title',
    #    'content',
    #    'thumbnail',
    #    'author',
    #    'slug'
    # )

    def get_context_data(self, **kwargs):
        """ pasar datos de contexto """

        context = super().get_context_data(**kwargs)
        # actualiza variable view_type de post_form.html
        context.update({
            'view_type': 'create'
        })
        return context


class PostUpdateView(UpdateView):
    # PostForm
    form_class = PostForm
    model = Post
    success_url = '/'
    # lista de campos que tiene el modelo Post a actualizar
    # al modificar post_form {{ form_type }}, pide eliminar los campos
    # fields = (
    #    'title',
    #    'content',
    #    'thumbnail',
    #    'author',
    #    'slug'
    # )

    def get_context_data(self, **kwargs):
        """ pasar datos de contexto """

        context = super().get_context_data(**kwargs)
        # actualiza variable view_type de post_form.html
        context.update({
            'view_type': 'update'
        })
        return context


class PostDeleteView(DeleteView):
    model = Post
    # redirecciona al mismo view que estamos viendo el listado de post = página principal
    success_url = '/'
