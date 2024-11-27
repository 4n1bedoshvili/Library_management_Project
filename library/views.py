from rest_framework import viewsets, filters
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Book, Borrow, Reservation
from .serializers import BookSerializer, BorrowSerializer
from rest_framework.pagination import PageNumberPagination


# Book filter class for search functionality

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    genre = django_filters.CharFilter(field_name='genre__name', lookup_expr='icontains')
    available = django_filters.BooleanFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'available']


# Pagination class for book lists
class BookPagination(PageNumberPagination):
    page_size = 10  # Define the number of books per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Optional: limit max number of books


# ViewSet for Book API
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = BookFilter
    ordering_fields = ['title', 'author', 'release_date']
    ordering = ['title']


# ViewSet for Borrow API (reservation handling)
class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


# Register user view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}, you have successfully registered!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'login.html', {'error': 'Both fields are required.'})

    return render(request, 'login.html')


# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')


# Home view
def home(request):
    return render(request, 'home.html')


# List of books with search functionality
def book_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(title__icontains=search_query)
    else:
        books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books})


# Book detail view
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


# Reservation functionality for users to borrow books
@login_required
def reserve_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Check if the book is available
    if book.available:
        book.available = False
        book.reserved_by = request.user
        book.reservation_date = timezone.now()
        book.save()

        # Create a reservation record
        Reservation.objects.create(user=request.user, book=book, reservation_date=timezone.now())

        return redirect('book_detail', book_id=book.id)

    return render(request, 'book_detail.html', {'book': book, 'error_message': 'This book is currently unavailable for reservation.'})


# Display borrowed books for the logged-in user
@login_required
def borrowed_books(request):
    # Fetch reservations for the logged-in user
    reservations = Reservation.objects.filter(user=request.user)

    return render(request, 'borrowed_books.html', {'reservations': reservations})
