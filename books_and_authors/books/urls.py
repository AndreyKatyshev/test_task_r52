from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('download', views.download_x2, name='download_x2'),
    path(
        'authors/<int:author_id>/',
        views.all_books_for_author,
        name='all_books_for_author'
    ),
    path('add_authors/', views.add_authors, name='add_authors'),
    path('add_authors_v2/', views.AddAuthors.as_view())
]
