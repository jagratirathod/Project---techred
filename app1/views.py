from django.shortcuts import render
from .models import Book
from django.http import HttpResponse


# Create your views here.



def test(request):
    return HttpResponse("Hello...")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


