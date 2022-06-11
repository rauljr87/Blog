from django.db import models


class Post(models.Model):
    """ Campos para los Posts """

    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # author = models.ForeignKey()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ Campos para los comentarios """

    # user = models.ForeignKey()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    """ Indica cuantas vistas ha tenido el post """

    # user = models.ForeignKey()
    # hacemos referencia al post con el que estamos haciendo los views
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
