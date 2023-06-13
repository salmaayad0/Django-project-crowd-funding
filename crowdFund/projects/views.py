from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Project

# Create your views here.
def index(request):
    return HttpResponse("projects")


# add project 
# def addProject(request):
#     if(request.method == 'POST'):
#         Project.objects.create(title = request.POST['title'],
#         userEmail = request.POST['email'],
#        details = request.POST['details'],
#        category = request.POST['category'],
#         mutliImage = request.POST['mutliImage'],
#         totalTarget = request.POST['totalTarget'],
#         tag = request.POST['tag'],
#         startDate = request.POST['startDate'])
        
#         return HttpResponseRedirect('/projects')
#     return render(request, 'projects/addProject.html')


    
