from django import forms


class SearchBookForm(forms.Form):
    keyWord = forms.CharField(required=False)