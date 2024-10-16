from django import forms
from booking.models import BookStatus
from django.forms import ModelForm
from manageBook.models import Book
from django.utils import timezone


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
        
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'publish_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean_publish_date(self):
        publish_date = self.cleaned_data.get('publish_date')
        if publish_date and publish_date > timezone.now().date():
            raise forms.ValidationError("The publish date cannot be in the future.")
        return publish_date

        
