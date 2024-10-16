from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class BookStatus(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status


class Cart(models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Cart of {self.member.first_name}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(
        'manageBook.Book', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.book.name} in cart of {self.cart.member.first_name}"


class BorrowBook(models.Model):
    history = models.ForeignKey(
        'booking.BorrowHistory', null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(
        'manageBook.Book', on_delete=models.CASCADE, null=True, blank=True)
    queue_date = models.DateField(null=True)
    borrow_date = models.DateField(null=True, blank=True)
    status = models.ForeignKey(BookStatus, default=1, on_delete=models.CASCADE)


class BorrowHistory(models.Model):
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='borrower')

    def __str__(self):
        return f"{self.member.first_name} borrow history for {self.borrow_date}"
