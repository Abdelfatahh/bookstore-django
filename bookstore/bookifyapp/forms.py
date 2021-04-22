from django import forms  
from bookifyapp.models import Book
from django.core.exceptions import ValidationError
class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("isbn_auto_generated_number",)


    def clean_book_name(self):
       
        book_name = self.cleaned_data.get("book_name")
        if len(book_name) > 50 or len(book_name) < 10 :
            raise ValidationError("Book name must be between 10 and 50 characters")
        return book_name


    




