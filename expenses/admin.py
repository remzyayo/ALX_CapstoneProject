from django.contrib import admin
from .models import Expense, Book, Borrower

admin.site.register(Expense)
admin.site.register(Book)
admin.site.register(Borrower)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author", "available")

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ("name", "book", "borrow_date", "status"),
    list_filter = ("status"),
    search_fields = ("name", "email","book__title")
