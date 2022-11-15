import csv
import json

from django.http import HttpResponse

from .models import Author, Book


def download_x2(request):
    """возвращает на скачивание файл CSV со списком книг
    у которых два или более автора."""
    general_books_list = Book.objects.all()
    desired_books = []
    for book in general_books_list:
        if len(book.authors.all()) > 1:
            desired_books.append(book)

    with open("books_m_a.txt", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file)
        file_writer.writerow(desired_books)

    with open("books_m_a.txt", encoding='utf-8') as file:
        return HttpResponse(file.read(),  content_type="text/csv")


def all_books_for_author(request, author_id):
    """Вщзвращает на страницу JSON
    в котором все книги автора по его ID.
    значение ID берётся из адресной строки"""
    general_books_list = Book.objects.filter(authors=author_id)
    desired_books = []
    for book in general_books_list:
        desired_books.append(book.title)
    return HttpResponse(
        json.dumps(desired_books), content_type='application/json'
    )


def add_authors(request):
    """принимает POST запрос с JSON в котором имена авторов.
    добавляет в базу данных имена которых ещё нет.
    При GET запросе подскажет что происходит."""
    existing_authors = [author.name for author in Author.objects.all()]
    if request.method == 'POST':
        response = ''
        for author in json.loads(request.body):
            name = author['name']
            if name in existing_authors:
                pass
                response += (f'{name} - уже есть в нашей базе, спасибо')
                response += '<br>'
            else:
                Author.objects.create(name=author['name'])
                name = author['name']
                response += (f'{name} - добавлен в список авторов')
                response += '<br>'
        return HttpResponse(response)
    if request.method == 'GET':
        response = (
            'Привет, по этому адресу нужно отправлять пост запрос с JSON '
            'в котором имена авторов, мы добавим их в нашу базу ' + '<br>'
            'А вот какие писатели нам уже известны:' + '<br>'
        )
        response += (',  '.join(existing_authors))
        return HttpResponse(response)
