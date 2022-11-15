from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length=150,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Book(models.Model):
    title = models.CharField(
        verbose_name='Название книги',
        max_length=150,
        unique=True,
    )
    authors = models.ManyToManyField(
        Author,
        related_name='book',
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title
