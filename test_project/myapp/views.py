from django.shortcuts import render
from .models import Book
from django.db.models import Q

def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'book_list.html', {'books': books})

def early_19s(request):
    books = Book.objects.filter(Q(published_date__year__gt=1900) & (Q(published_date__year__lt=1950)))
    return render(request, 'early_19s.html', {'books': books})

def late_19s(request):
    books = Book.objects.filter(Q(published_date__year__gt=1951) & (Q(published_date__year__lt=2000)))
    return render(request, 'late_19s.html', {'books': books})

def early_20s(request):
    books = Book.objects.filter(Q(published_date__year__gt=2000) & (Q(published_date__year__lt=2050)))
    return render(request, 'early_20s.html', {'books': books})

