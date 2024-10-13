from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q

# Create your views here.


class index(View):
    def get(self, request):
        return render(request, "test.html")
