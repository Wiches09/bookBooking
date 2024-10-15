from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.http import HttpRequest
from booking.models import *
from manageBook.models import *
from django.shortcuts import get_object_or_404


# Create your views here.
class QueueManagementView(View):
    def get(self, request: HttpRequest):
        book = Book.objects.all()
        context = {
            "book": book
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
