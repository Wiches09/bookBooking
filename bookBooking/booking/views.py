from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.http import HttpRequest
from booking.models import *
from manageBook.models import *
from django.shortcuts import get_object_or_404
from datetime import date, time
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse

# Create your views here.


class IndexView(View):
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


class BookDetailView(View):
    def get(self, request, book_id):
        book_detail = Book.objects.get(id=book_id)
        cart, created = Cart.objects.get_or_create(member_id=request.user.id)
        book_in_cart = CartItem.objects.filter(
            cart=cart, book=book_detail.id).exists()

        return render(request, "book-detail.html", {
            "book_detail": book_detail,
            "book_in_cart": book_in_cart,
        })

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        cart, created = Cart.objects.get_or_create(member_id=request.user.id)
        
        book_in_cart = CartItem.objects.filter(cart=cart, book=book).exists()
        if not book_in_cart:
            CartItem.objects.create(cart=cart, book=book)

        return redirect(reverse('book-detail', args=[book.id]))


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(member=request.user)
        items = cart.items.all()

        return render(request, "cart.html", {'items': items, 'cart': cart})

class ConfirmBooking(View):
    def post(self, request, cart_id):
        cart = get_object_or_404(Cart, id=cart_id)
        books_in_cart = CartItem.objects.filter(cart=cart)
        
        for cart_item in books_in_cart:
            book = cart_item.book
            BorrowHistory.objects.create(member=request.user, book=book)
            
        cart.items.all().delete()
            
        return redirect('index')