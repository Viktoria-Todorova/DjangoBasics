from django.db.models import Avg, Q
from django.forms import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookFormBasic, BookEditForm, BookDeleteForm, BookSearchForm
from books.models import Book


# Create your views here.
def lending_page(request: HttpRequest) -> HttpResponse:
    total_books = Book.objects.count()
    latest_book = Book.objects.order_by('-publishing_date').first()
    context = {
        'total_books': total_books,
        'latest_book': latest_book,
        'page_title': 'Home'
    }
    return render(request,'books/landing_page.html',context)

def books_list(request: HttpRequest) -> HttpResponse:
    search_form = BookSearchForm(request.GET or None)
    list_books = Book.objects.all()

    if search_form.is_valid():
        search_value = search_form.cleaned_data.get('query')
        if search_value:
            words = search_value.split()  # split into words
            query = Q()
            for word in words:
                query |= Q(title__icontains=word) | Q(description__icontains=word)
            list_books = list_books.filter(query)


    # if 'query' in request.GET:
    #     if search_form.is_valid():
    #         search_value = search_form.cleaned_data['query']
    #         list_books=list_books.filter(
    #             Q(title__icontains=search_value) |
    #             Q(description__icontains=search_value)
    #         )

    list_books = list_books.annotate(
        avg_rating=Avg('review__rating'),
    ).order_by('title')

    context = {
        'books': list_books,
        'page_title': 'Dashboard',
        'search_form': search_form,
    }

    return render(request, 'books/list.html',context)

def book_details(request: HttpRequest, slug:str) -> HttpResponse:
    book=get_object_or_404(
        Book.objects.annotate(
            avg_rating=Avg('review__rating'),
        ),slug=slug
    )

    context = {
        'book': book,
        'page_title': f'{book.title} details',
    }

    return render(request,'books/detail.html',context)


def book_create(request: HttpRequest) -> HttpResponse:
    if request.user.is_staff:
        BookForm = modelform_factory(Book,fields="__all__")
    else:
        BookForm =modelform_factory(Book,exclude=['slug'])
    form = BookForm(request.POST or None,request.FILES)
    if request.method == 'POST' and form.is_valid():
        # Book.objects.create(
        #     title=form.cleaned_data['title'],
        #     publishing_date=form.cleaned_data['publishing_date'],
        #     isbn=form.cleaned_data['isbn'],
        #     genre=form.cleaned_data['genre'],
        #     price=form.cleaned_data['price'],
        #     description=form.cleaned_data['description'],
        #     image_url=form.cleaned_data['image_url'],
        #     publisher=form.cleaned_data['publisher'],
        #     #or!!!!!!!!!!!!!!!! **form.cleaned_data !!!!!!!!!!!!!!!!!
        #
        # )   ->> for forms
        form.save() #--> to have save() method we have to have an instantion
        return redirect('books:home')

    context = {
        'form': form,
    }

    return render(request,'books/create.html',context)


def book_edit(request: HttpRequest,pk:int) -> HttpResponse:
    book = Book.objects.get(pk=pk)
    form= BookEditForm(request.POST or None,instance=book)  #we have instance only for forms
    if request.method == 'POST' and form.is_valid():
        form.save() #--> to have save() method we have to have an instantion
        return redirect('books:home')

    context = {
        'form': form,
    }

    return render(request,'books/edit.html',context)


def book_delete(request: HttpRequest,pk:int) -> HttpResponse:
    book = Book.objects.get(pk=pk)
    form= BookDeleteForm(request.POST or None,instance=book)  #we have instance only for forms
    if request.method == 'POST' and form.is_valid():
        book.delete()
        return redirect('books:home')

    context = {
        'form': form,
    }

    return render(request,'books/delete.html',context)