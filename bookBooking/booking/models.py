from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Member(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Staff(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookStatus(models.Model):
    # e.g., available, borrowed, reserved
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status


class Cart(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    create_date = models.DateField()

    def __str__(self):
        return f"Cart of {self.member.first_name}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey('manageBook.Book', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.name} in cart of {self.cart.member.first_name}"


class BorrowBook(models.Model):
    borrow_history = models.ForeignKey(
        'BorrowHistory', on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(
        'manageBook.Book', on_delete=models.CASCADE, null=True, blank=True)


class BorrowHistory(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    book_returned = models.DateField(null=True, blank=True)
    fine = models.DecimalField(decimal_places=2, max_digits=5)
    status = models.ForeignKey(BookStatus, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)

    position_in_queue = models.PositiveIntegerField(null=True, blank=True)
    queue_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.member.first_name} borrow history for {self.borrow_date}"
