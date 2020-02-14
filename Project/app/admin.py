from django.contrib import admin
from app.models import Book, Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'ctype', 'created', 'updated')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'desc', 'created', 'updated')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)