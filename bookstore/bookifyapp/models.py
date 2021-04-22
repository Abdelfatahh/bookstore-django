from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Categories"

    def clean(self): 
        name = self.name
        if len(name) < 2:
            raise ValidationError("Category name is less than 2 characters???")
        return self.name


    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    book_name = models.CharField(max_length=256)
    book_price = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="books")
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    isbn_auto_generated_number = models.UUIDField(default=uuid.uuid4, editable=False)
    class Meta:
        db_table = "books"
    def __str__ (self):
        return self.book_name