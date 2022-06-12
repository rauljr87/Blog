# Vistas basadas en clases
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, PostView, Like
# class form, se los debe especificar en los modelos de PostCreateView y PostUpdateView
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        # en caso de usuarios anónimos
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)

        return object


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


def like(request, slug):
    """ conteo de likes """
    post = get_object_or_404(Post, slug=slug)
    # en caso de usuarios anónimos
    if request.user.is_authenticated:
        # queryset
        like_qs = Like.objects.filter(user=request.user, post=post)
        if like_qs.exists():
            like_qs[0].delete()
            return redirect('detail', slug=slug)
        Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)

