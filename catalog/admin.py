from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


class BookInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline,]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# 'display_genre'는 Book 모델에 있는 function이름임, ManyToManyField 에서는 필드이름 바로적용 불가.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'display_genre', 'language')
    inlines = [BooksInstanceInline,]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'imprint', 'id', 'status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'borrower', 'due_back')}),
    )

admin.site.register(Genre)
admin.site.register(Language)
