from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    publish_date = models.DateField()
    categories = models.ManyToManyField("booking.Category")
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


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
    status = models.CharField(max_length=10)


class Cart(models.Model):
    member_id = models.ForeignKey("booking.Member", on_delete=models.CASCADE)
    create_date = models.DateField()


class CartItem(models.Model):
    cart_id = models.ForeignKey("booking.Cart", on_delete=models.CASCADE)
    book_id = models.ForeignKey("booking.Book", on_delete=models.CASCADE)


class BorrowBook(models.Model):
    borrow_history_id = models.ForeignKey(
        "booking.borrowHistory", on_delete=models.CASCADE)
    book_id = models.ForeignKey("booking.Book", on_delete=models.CASCADE)


class BorrowHistory(models.Model):
    borrow_id = models.ForeignKey(
        "booking.BorrowBook", on_delete=models.CASCADE)
    member_id = models.ForeignKey("booking.Member", on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now=False, auto_now_add=False)
    return_date = models.DateField(auto_now=False, auto_now_add=False)
    book_returned = models.DateField(auto_now=False, auto_now_add=False)
    fine = models.DecimalField(decimal_places=2, max_digits=5)
    status = models.ForeignKey("booking.BookStatus", on_delete=models.CASCADE)
    staff_id = models.ForeignKey("booking.Staff", on_delete=models.CASCADE)
