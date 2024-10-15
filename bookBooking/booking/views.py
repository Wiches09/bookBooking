from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.http import HttpRequest
from booking.models import *
from manageBook.models import *

# Create your views here.


class Index(View):
    def get(self, request):
        query = request.GET

        if query.get("search"):
            books = Book.objects.filter(
                Q(name__icontains=query.get("search")) |
                Q(author__icontains=query.get("search")) |
                Q(categories__name__icontains=query.get("search"))
            )
        else:
            books = Book.objects.all()

        return render(request, "index.html", {
            "books": books
        })
