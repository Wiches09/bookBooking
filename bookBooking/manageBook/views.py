from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q

# Create your views here.
class BookManagement(View):
    def get(self, request):
        return 0