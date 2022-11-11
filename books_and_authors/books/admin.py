from django.contrib import admin

from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):

    list_display = ('name', 'pk', 'book',)
    empty_value_display = '-пусто-'


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'pk',)
    empty_value_display = '-пусто-'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
