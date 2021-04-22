from django.contrib import admin
from bookifyapp.models import Book, Category,Tag
from .forms import bookForm
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    form = bookForm
    list_display = ("id", "book_name","book_price", "author")
    list_filter = ("categories",)
    search_fields = ("book_name",)



class BookInline(admin.StackedInline):

    model = Book
    max_num = 3
    extra = 1

class TagAdmin(admin.ModelAdmin): 
    inlines = [BookInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Tag, TagAdmin)
