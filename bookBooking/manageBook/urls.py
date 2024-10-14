from django.urls import path, include
from . import views

urlpatterns = [
    path("manage_index/", views.index.as_view(), name="index")
]
