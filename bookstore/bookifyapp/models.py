from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=256)
    book_price = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    class Meta:
        db_table = "books"
    def __str__ (self):
        return self.book_name