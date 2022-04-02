

from django.contrib import admin
from django.urls import path, include
from .views import LibraryView, AuthorController, book_detail, author_detail

urlpatterns = [
    path('book/', LibraryView.as_view(), name='book'),
    path('book/<int:pk>', book_detail),
    path('author/', AuthorController.as_view(), name='author'),
    path('author/<int:pk>', author_detail),
]
