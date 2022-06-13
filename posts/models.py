from django.db import models
# Usuario de autenticación, importamos usuario base AbstracUser
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    """ Usuario de autenticación
     AbstractUser se encarga de username, password, email """
    pass

    def __str__(self):
        return self.username


# Indicar a django que estamos usando nuestro modelo allauth, especificarlo en settings


class Post(models.Model):
    """ Campos para el Post """

    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # campo para trabajar con el slug de las url, nombre para la página
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Obtiene url y retorna a view detail
        Pasamos esta función en nuestro post_list.html """
        return reverse("detail", kwargs={
            'slug': self.slug
        })

    def get_like_url(self):
        """ Obtiene número de likes y retorna a view detail
        Pasamos esta función en nuestro post_list.html """
        return reverse("like", kwargs={
            'slug': self.slug
        })

    # define los comments para poder mostrarlos a través del template
    @property
    def comments(self):
        return self.comment_set.all()

    # para contar los comments
    @property
    def get_comment_count(self):
        # query de comentarios
        return self.comment_set.all().count()

    # para contar las views
    @property
    def get_view_count(self):
        # query de comentarios
        return self.postview_set.all().count()

    # para contar los likes
    @property
    def get_like_count(self):
        # query de comentarios
        return self.like_set.all().count()


class Comment(models.Model):
    """ Campos para los comentarios """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    """ Indica cuantas vistas tiene el post """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # para referencia del post al cual se hacen las visualizaciones
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    """ Indica cuantos likes tiene un post """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # para referencia del post al cual se hacen los likes
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
