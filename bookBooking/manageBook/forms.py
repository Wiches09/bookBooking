from django import forms
from booking.models import BookStatus
from django.forms import ModelForm
from manageBook.models import Book


class SearchBookForm(forms.Form):
    keyWord = forms.CharField(required=False)


class BookStatusForm(forms.Form):
    status = forms.ModelChoiceField(
        queryset=BookStatus.objects.all(),
        label="Select Status",
    )


class AddBookForm(ModelForm):
    
    
    class Meta:
        model = Book
        fields = [
            'name',
            'author',
            'publisher',
            'publish_date',
            'categories',
            'description',
        ]
