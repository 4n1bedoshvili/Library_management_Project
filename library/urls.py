from django.contrib.auth import views as auth_views
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import BookViewSet, BorrowViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'borrows', BorrowViewSet)


urlpatterns = [
    path('api/', include(router.urls)),  # API routes
    path('accounts/register/', views.register, name='register'),  # Register route
    path('accounts/login/', views.login_view, name='login'),  # Login route
    path('accounts/logout/', views.logout_view, name='logout'),  # Logout route
    path('', views.home, name='home'),  # Home route
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/reserve/<int:book_id>/', views.reserve_book, name='reserve_book'),
    path('api/', include(router.urls)),
    path('borrowed-books/', views.borrowed_books, name='borrowed_books'),
    path('book/<int:book_id>/reserve/', views.reserve_book, name='reserve_book'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),

]
