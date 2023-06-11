from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Users, Login
from .forms import LoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
     loginData = LoginForm(request.POST)
     data = Users.objects.all()
     if loginData.is_valid():
         email = request.POST.get('email')
         password = request.POST.get('password')
         print(email)
         for user in data:
             dbEmail = user.email
             dbpassword = user.password
             print(dbEmail)
             if email == dbEmail and password == dbpassword:
                user = {
                'email': email,
                'password': password }
                return HttpResponse('users/index.html')
             else:
                return HttpResponse('users/register.html')
        
    return render(request, 'users/login.html', {'formLogin':LoginForm})
