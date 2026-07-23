from django.contrib import admin
from .models import Expense, Book, Borrower, Recipe, Category, Project, Task

admin.site.register(Expense)
admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Task)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author", "available")

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ("name", "book", "borrow_date", "status"),
    list_filter = ("status"),
    search_fields = ("name", "email","book__title")

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "cook_time", "instructions")
    list_filter = ("category")
    search_fields = ("title", "ingredients")

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title",) 

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "priority", "status", "deadline",)
    list_filter = ("priority", "status", "project",)
    search_fields = ("title", "Project__title",)
