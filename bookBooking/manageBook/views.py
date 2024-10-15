from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.http import HttpRequest
from booking.models import *
from manageBook.models import *
from django.shortcuts import get_object_or_404
from manageBook.forms import *


# Create your views here.
class QueueManagementView(View):
    def get(self, request: HttpRequest):
        book = Book.objects.all()
        form = SearchBookForm()
        context = {
            "books": book,
            "form": form
        }
        return render(request, "indexStaff.html", context)

    def post(self, request: HttpRequest):
        form = SearchBookForm(request.POST)
        book = Book.objects.all()

        if form.is_valid():
            query = form.cleaned_data['keyWord']
            book = Book.objects.filter(name__icontains=query)

        context = {
            "books": book,
            "form": form
        }
        return render(request, "indexStaff.html", context)


class QueueDetailView(View):
    def get(self, request: HttpRequest, pk):
        book = get_object_or_404(Book, pk=pk)
        # form = BookForm(instance=book)
        context = {
            "book": book,
            # "form": form
        }
        return render(request, "queueDetail.html", context)
