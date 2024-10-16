from django.urls import path, include
from . import views

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("cart/", views.CartView.as_view(), name="cart")
]
