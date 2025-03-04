from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def homepage(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm(instance=book)
    return render(request, 'add_book.html', {'form': form})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book:
        book.delete()
    return redirect('homepage')