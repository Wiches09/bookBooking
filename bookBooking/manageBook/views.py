from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.http import HttpRequest
from booking.models import *
from manageBook.models import *
from django.shortcuts import get_object_or_404
from manageBook.forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


# Create your views here.
class QueueManagementView(PermissionRequiredMixin, LoginRequiredMixin, View):
    login_url = '/authen/'
    permission_required = ["booking.change_bookstatus"]

    def get(self, request: HttpRequest):
        books = Book.objects.all()
        form = SearchBookForm()
        context = {
            "books": books,
            "form": form
        }
        return render(request, "indexStaff.html", context)

    def post(self, request: HttpRequest):
        form = SearchBookForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['keyWord']
            if query:
                books = Book.objects.filter(name__icontains=query)
            else:
                books = Book.objects.all()
        else:
            books = Book.objects.all()

        context = {
            "books": books,
            "form": form
        }
        return render(request, "indexStaff.html", context)


class QueueDetailView(PermissionRequiredMixin, LoginRequiredMixin, View):
    login_url = '/authen/'
    permission_required = ["booking.change_bookstatus"]

    def get(self, request: HttpRequest, pk):
        books = get_object_or_404(Book, pk=pk)
        queue = BorrowBook.objects.filter(book=books, status_id__in=[
                                          1, 2, 3]).select_related('history').order_by('queue_date')
        form = BookStatusForm()

        queue_context = []
        for queue_item in queue:
            form = BookStatusForm(initial={'status': queue_item.status})
            queue_context.append({
                'queue_item': queue_item,
                'form': form,
            })

        context = {
            'book': books,
            'queue': queue_context,
        }
        return render(request, "detailQueue.html", context)

    def post(self, request, pk):
        books = get_object_or_404(Book, pk=pk)
        queue_item_id = request.POST.get('queue_item_id')
        queue_item = get_object_or_404(BorrowBook, id=queue_item_id)

        form = BookStatusForm(request.POST)

        if form.is_valid():
            selected_status = form.cleaned_data['status']
            queue_item.status = selected_status
            queue_item.save()

            return redirect('queueDetail', pk=books.pk)

        return render(request, "detailQueue.html", {'form': form, 'book': books})


class AddBook(PermissionRequiredMixin, LoginRequiredMixin, View):
    login_url = '/authen/'
    permission_required = ["booking.change_bookstatus"]
    
    def get(self, request: HttpRequest):
        form = AddBookForm()
        return render(request, "addBook.html", {'form': form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addBook')
        else:
            form = AddBookForm()
        return render(request, 'addBook.html', {'form': form})
