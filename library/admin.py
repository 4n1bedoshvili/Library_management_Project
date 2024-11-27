# admin.py
from django.contrib import admin
from .models import CustomUser, Author, Book, Borrow

class BorrowInline(admin.TabularInline):
    model = Borrow
    extra = 0

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author__name', 'description']
    list_filter = ['available', 'release_date']
    inlines = [BorrowInline]
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'borrow_date', 'return_date']
    list_filter = ['borrow_date', 'return_date']
    search_fields = ['user__username', 'book__title']

admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)
