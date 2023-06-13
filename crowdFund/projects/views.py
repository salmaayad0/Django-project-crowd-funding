from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Project

# add project 
def addProject(request):
    if(request.method == 'POST'):
        
        return HttpResponseRedirect('/projects')
    return render(request, 'projects/addProject.html')


# projects category 
# eduaction
def edu_category(request):
    selectedProj = []
    projects = Project.objects.all()
    for project in projects:
        if project.category == 'education':
            selectedProj.append(project)
    return render(request, 'projects/education.html', {'projects': selectedProj})

# entertainment
def entertainment_category(request):
    selectedProj = []
    projects = Project.objects.all()
    for project in projects:
        if project.category == 'entertainment':
            selectedProj.append(project)
    return render(request, 'projects/entertainment.html', {'projects': selectedProj})


# sports
def sports_category(request):
    selectedProj = []
    projects = Project.objects.all()
    for project in projects:
        if project.category == 'sports':
            selectedProj.append(project)
    return render(request, 'projects/sports.html', {'projects': selectedProj})


# fashon
def fashon_category(request):
    selectedProj = []
    projects = Project.objects.all()
    for project in projects:
        if project.category == 'fashon':
            selectedProj.append(project)
    return render(request, 'projects/fashon.html', {'projects': selectedProj})

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


    
