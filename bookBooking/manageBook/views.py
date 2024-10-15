from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.http import HttpRequest


# Create your views here.
class QueueManagement(View):
    def get(self, request: HttpRequest):
        return render(request, "indexStaff.html")