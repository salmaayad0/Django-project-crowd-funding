from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Project

# Create your views here.
def index(request):
    return HttpResponse("projects")


# add project 
def addProject(request):
    if(request.method == 'POST'):
        Project.objects.create(title = request.POST['title'])
        Project.objects.create(details = request.POST['details'])
        Project.objects.create(category = request.POST['category'])
        Project.objects.create(mutliImage = request.POST['mutliImage'])
        Project.objects.create(totalTarget = request.POST['totalTarget'])
        Project.objects.create(tag = request.POST['tag'])
        Project.objects.create(startDate = request.POST['startDate'])
        
        return HttpResponseRedirect('/projects')
    return render(request, 'projects/addProject.html')