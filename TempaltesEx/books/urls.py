from django.urls import path, include

from books.views import lending_page, books_list, book_details

app_name = 'books'
books_patterns = [
    path('', books_list,name='list'),
    path('<slug:slug>/',book_details,name='detail'),
]
urlpatterns = [
    path('',lending_page,name='home'),
    path('books/', include(books_patterns)),]

