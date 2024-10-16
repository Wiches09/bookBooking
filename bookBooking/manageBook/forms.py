from django import forms
from booking.models import BookStatus


class SearchBookForm(forms.Form):
    keyWord = forms.CharField(required=False)


class BookStatusForm(forms.Form):
    status = forms.ModelChoiceField(
        queryset=BookStatus.objects.all(),
        label="Select Status",
    )
