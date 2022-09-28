from cmath import isnan
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from core.models import Library, Book

# Create your views here.
l = Library()

def home(request):
    return render(request, 'core/home.html')

def book_list(request):
    context = {'context' : l.list_books, "filter_year":2013} 
    #el filter_year define 2014 como una variable creando un filtro
    return render(request, 'core/book_list.html', context)



def book_register(request):
    return render(request, 'core/book_register.html')

def book_created(request):
    isbn = request.POST.get('isbn')
    title = request.POST.get('title')
    year = request.POST.get('year')
    autor = request.POST.get("autor")

    b = Book(isbn, title, year,autor)

    response = l.add_book(b)

    context = {'context':response}

    return render(request, 'core/book_created.html', context)

def book_deleted(request):
    isbn = request.POST.get('isbn')

    response = l.delete_book(isbn)

    context = {'context':response}

    return render(request, 'core/book_deleted.html', context)
