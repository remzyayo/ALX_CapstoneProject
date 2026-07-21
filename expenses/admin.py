from django.contrib import admin
from .models import Expense, Book, Borrower

admin.site.register(Expense)
admin.site.register(Book)
admin.site.register(Borrower)

