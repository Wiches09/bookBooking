from django.urls import path, include
from . import views

urlpatterns = [

    path("index/", views.QueueManagement.as_view(), name="manageBook")
]
