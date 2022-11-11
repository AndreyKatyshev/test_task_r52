# from django.shortcuts import get_object_or_404
# import requests
# import csv

from .models import Author, Book


def download_x2():
    books_list = Book.objects.all
    print(books_list)

# def all_books_by_authors(request, author_id):
#     books = get_object_or_404(Book, pk=author_id)
#     # response = requests.get('')
#     # characters = response.json().get('results')

# def add_author():
#     pass

# download_x2()