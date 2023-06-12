from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect  
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Users, Login
from .forms import LoginForm,RegForm
from django.db import models 
from projects.models import Project

# Create your views here.

#home function
def home(request,userEmail_id):
    data = Users.objects.get(email=userEmail_id)
    return render(request, 'users/home.html',{"data":data})


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
                     return HttpResponseRedirect(f"/home/{email}")

            else:
                 return HttpResponseRedirect("/login")
    return render(request, 'users/login.html', {'formLogin':LoginForm})



def verification(request):
    return render(request, 'users/verification.html')


def list_users(request):
    data=Users.objects.all()
    return render(request,"users/allusers.html",{"users":data})


# regesteration function
def registeration(request):
    if request.method == "POST":
        data=RegForm(request.POST)
        if data.is_valid():
            userdata=Users.objects.all()
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
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
 


def View(request):
        data = Project.objects.all()
        projects = []
        for project in data:
           
            projects.append(project)
            print(f"{projects}")
             
      
        return render(request,"users/allprojects.html", {"projects":projects})

def view_project(request,userEmail_id)   :
       
        print(userEmail_id)
        data = Project.objects.all()
        for project in data:
             emails=[]
             emails.append(project.userEmail)
             if str(userEmail_id)== str(emails[0]):
                 show=Project.objects.get(userEmail_id=project.userEmail)
                 return render(request,"users/user_project.html",{"project":show})
             
        
        return render(request,"users/show_userproject.html")


def update_user(request,userEmail_id):
        data = Users.objects.get(email=userEmail_id)

        if (request.method=="POST"):
            Users.objects.filter(email=userEmail_id).update(first_name=request.POST['first_name'],
                                                       last_name=request.POST['last_name'],
                                                       password=request.POST['password'],
                                                       image=request.POST['image']     ,                                              
                                                       phone_number=request.POST['phone_number']                   )
            
            return HttpResponseRedirect(f"/profile/{userEmail_id}")
        return render(request,"users/update_user.html",{"user":data})


# delete account 
def delete_user(request, userEmail_id):
    Users.objects.filter(email = userEmail_id).delete()
    return HttpResponseRedirect('/')


# profile 
def userProfile(request, userEmail_id):
    user = Users.objects.get(email = userEmail_id)
    return render(request,"users/profile.html", {"user":user})
