from django import forms
from .models import Book, Author, Genre, Language, BookInstance

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'imprint', 'ISBN', 'genre', 'language', 'price', 'unit', 'age_restriction']
        widgets = {
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'genre': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'age_restriction': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '21'}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth', 'date_of_death']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_of_death': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']

class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book', 'uniqueId', 'status', 'due_back']
        widgets = {
            'due_back': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        } 