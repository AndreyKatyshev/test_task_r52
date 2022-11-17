import io
import csv
import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Author, Book


def download_x2(request):
    """возвращает на скачивание файл CSV со списком книг
    у которых два или более автора."""
    general_books_list = Book.objects.all()
    desired_books = []
    for book in general_books_list:
        if len(book.authors.all()) > 1:
            desired_books.append(book.title)
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(desired_books)
    return HttpResponse(buffer.getvalue(),  content_type="text/csv")


def all_books_for_author(request, author_id):
    """Вщзвращает на страницу JSON
    в котором все книги автора по его ID.
    значение ID берётся из адресной строки"""
    general_books_list = Book.objects.filter(authors=author_id)
    desired_books = []
    for book in general_books_list:
        desired_books.append(book.title)
    return JsonResponse(desired_books, safe=False)


class AddAuthors(View):

    def post(self, request):
        response = ''
        for author in json.loads(request.body):
            existing_authors = [author.name for author in Author.objects.all()]
            name = author['name']
            if name in existing_authors:
                response += (f'{name} - уже есть в нашей базе, спасибо')
                response += '<br>'
            else:
                Author.objects.create(name=author['name'])
                response += (f'{name} - добавлен в список авторов')
                response += '<br>'
        return HttpResponse(response)

    def get(self, request):
        existing_authors = [author.name for author in Author.objects.all()]
        response = (
            'Привет, по этому адресу нужно отправлять пост запрос с JSON '
            'в котором имена авторов, мы добавим их в нашу базу.' + '<br>'
            'А вот какие писатели нам уже известны:' + '<br>'
        )
        response += (',  '.join(existing_authors))
        return HttpResponse(response)
