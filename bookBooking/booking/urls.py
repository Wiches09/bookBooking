from django.urls import path, include
from . import views

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart/<int:cart_id>/", views.ConfirmBooking.as_view(),
         name="confirm_booking"),
    path("cart/<int:cart_id>/<int:book_id>",
         views.RemoveBookFromCart.as_view(), name="remove_book"),
    path("index/<int:book_id>", views.BookDetailView.as_view(), name="book-detail"),
    path("history/", views.BorrowHistoryView.as_view(), name="history")
]
