<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect  
=======
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
>>>>>>> 9bc522e9a3258eb9f6dc9e7a0f8db2b4ded41120

from .models import Users, Login
from .forms import LoginForm,RegForm

# Create your views here.

#login function
def login(request):
    if request.method == 'POST':
     loginData = LoginForm(request.POST)
     if loginData.is_valid():
            userdata=Users.objects.all()
            email=request.POST.get('email')
            password=request.POST.get('password')
            print(email)
            emails=[]
            for user in userdata:
                print(user.email)
                print(user.password)
                emails.append(user.email)
                print(emails)
            if email in emails  :
                    print("email already exist")
                    if user.password==password :
                     return HttpResponseRedirect("/index")

            else:
                 return HttpResponseRedirect("/login")
    return render(request, 'users/login.html', {'formLogin':LoginForm})

def verification(request):


    return render(request, 'users/verification.html')
def index(request):


    return render(request, 'users/index.html')



<<<<<<< HEAD

# regesteration function

=======
>>>>>>> 9bc522e9a3258eb9f6dc9e7a0f8db2b4ded41120
def registeration(request):
    if request.method == "POST":
        data=RegForm(request.POST)
        if data.is_valid():
            userdata=Users.objects.all()
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            # print(email)
            emails=[]
            for user in userdata:
                print(user.email)
                emails.append(user.email)
                print(emails)
            if email in emails  :
                    print("email already exist") 
                    
            else:
                    if password==confirm_password:
                        data.save()
                        return HttpResponseRedirect("/verification")
                    
    
                    else:
                        return render(request,"users/errorpass.html")
        else:
                print("invalid data")      
    return render(request,"users/register.html", {"lf":RegForm})
 
