from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.http import HttpRequest
from booking.models import *
from manageBook.models import *
from django.shortcuts import get_object_or_404
from datetime import date, time
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

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


class BookDetail(View):
    def get(self, request, book_id):
        book_detail = Book.objects.get(id=book_id)
        cart, created = Cart.objects.get_or_create(member_id=request.user.id)
        book_in_cart = CartItem.objects.filter(cart=cart, book=book_detail.id).exists()
        
        return render(request, "book-detail.html", {
            "book_detail" : book_detail,
            "book_in_cart" : book_in_cart
        })


class AddToCart(View):
    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        cart, created = Cart.objects.get_or_create(member_id=request.user.id)
        cart_item = CartItem.objects.create(cart=cart, book=book)

        

        return redirect(request, "book-detail.html")


class CartView(View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(member=request.user)
        items = cart.items.all()
        
        return render(request, "cart.html", {'items': items})