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
    create_date = models.DateField()

    def __str__(self):
        return f"Cart of {self.member.first_name}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(
        'manageBook.Book', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.book.name} in cart of {self.cart.member.first_name}"


class BorrowBook(models.Model):
    borrow_history = models.ForeignKey(
        'BorrowHistory', on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(
        'manageBook.Book', on_delete=models.CASCADE, null=True, blank=True)


class BorrowHistory(models.Model):
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='borrower')
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    book_returned = models.DateField(null=True, blank=True)
    fine = models.DecimalField(decimal_places=2, max_digits=5)
    status = models.ForeignKey(BookStatus, on_delete=models.CASCADE)
    staff = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='approver')

    position_in_queue = models.PositiveIntegerField(null=True, blank=True)
    queue_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(
        'manageBook.Book', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.member.first_name} borrow history for {self.borrow_date}"
