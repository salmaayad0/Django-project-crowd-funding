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
 





# ------------------------------------------------------------------------------------------ #
def View(request):
        print("------------View Project----------------")
    # try:
    #     readfile = open("projects.txt")
    # except:
    #     print("File Doesnt Exit")
    # else:
        # read data from file

        data = Project.objects.all()
        projects = []
        for project in data:
            # project.title
            # project.details
            # project.category
            # project.mutliImage
            # project.totalTarget
            # project.tag
            # project.startDate
            # project.email
            projects.append(project)
        # for project in projects:
        #     projectsdetails = project.split(",")
        #     if projectsdetails[7] == email:
        #         print("----------------Projects----------------")
            print(f"{projects}")
             
        # else:
        #      print("This user doesnt have any projects to view")
        return render(request,"users/allprojects.html", {"projects":projects})

def view_project(request,email)   :
        # email=request.POST.get('email')
        data = Project.objects.all()
        for project in data:
             print(project.userEmail)
             if project.userEmail ==email:
                  show=Project.objects.get(email=project.userEmail)
        return render(request,"users/allproject.html", {"project":show})
