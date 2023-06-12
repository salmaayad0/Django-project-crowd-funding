from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Users, Login
from .forms import LoginForm,RegForm

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
             if email == dbEmail & password == dbpassword:
                user = {
                'email': email,
                'password': password 
                }
                return HttpResponse('users/index.html')
             else:
                return HttpResponse('users/register.html')
        
    return render(request, 'users/login.html', {'formLogin':LoginForm})




def registeration(request):
    if request.method == "POST":
        data=RegForm(request.POST)
        if data.is_valid():
            userdata=Users.objects.all()
            email=request.POST.get('email')
            print(email)
            emails=[]
            for user in userdata:
                print(user.email)
                emails.append(user.email)
                print(emails)
            if email in emails  :
                    print("email already exist") 
                    
            else:
                    data.save()
                    
    
        
        else:
                print("invalid data")      
    return render(request,"users/register.html", {"lf":RegForm})
 
