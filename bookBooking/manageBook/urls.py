from django.urls import path, include
from . import views

urlpatterns = [
    path("index/", views.QueueManagementView.as_view(), name="manageBook"),
    path("index/search/", views.QueueManagementView.as_view(), name="searchBook"),
    path("index/detail/<int:pk>",
         views.QueueDetailView.as_view(), name="queueDetail"),
    path("index/addBook/", views.AddBook.as_view(), name="addBook")
]
