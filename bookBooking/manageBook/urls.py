from django.urls import path, include
from . import views

urlpatterns = [

    path("index/", views.QueueManagementView.as_view(), name="manageBook")
]
