from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect  
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


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




# regesteration function
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
 

# delete account 
def deleteUser(request, email):
    Users.objects.filter(email = email).delete()
    return HttpResponseRedirect('')


# profile 
def userProfile(request, email):
    user = Users.objects.get(email = email)
    return render(request,"users/profile.html", {"user":user})