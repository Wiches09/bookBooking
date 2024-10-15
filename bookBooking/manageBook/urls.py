from django.urls import path, include
from . import views

urlpatterns = [

    path("index/", views.BookManagement.as_view(), name="manageBook")
]
