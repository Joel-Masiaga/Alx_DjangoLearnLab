from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)


class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=100, required=True)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        return author
