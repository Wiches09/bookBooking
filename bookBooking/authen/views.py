from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(View):

    def get(self, request):
        # code here
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": None})
    
    def post(self, request):
        # code here
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        return render(request,'login.html', {"form":form})


class LogoutView(LoginRequiredMixin, View):
    login_url = '/authen/'
    def get(self, request):
        # code here
        logout(request)
        return redirect('login')
    
# class RegisterView(View):
#     def get(self, request):
#         # code here
#         form = RegisterForm(request.POST)
    
#     def post(self, request):
#         # code here
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('index')
#         return render(request,'login.html', {"form":form})