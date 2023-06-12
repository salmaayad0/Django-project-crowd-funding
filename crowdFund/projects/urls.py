from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('/addproject', views.addProject, name='addProject')
]
