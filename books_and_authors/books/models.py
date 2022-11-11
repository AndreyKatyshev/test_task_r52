from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Author(models.Model):
    name = models.CharField(
        verbose_name = 'Автор',
        max_length=150,
        unique=True,
        # db_index=True,
    )

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(
        verbose_name = 'Название книги',
        max_length=150,
        unique=True,
        # db_index=True,
    )
    author = models.ManyToManyField(
        Author,
        related_name='book',
        # db_index=True,
    )

    def __str__(self):
        return self.title
