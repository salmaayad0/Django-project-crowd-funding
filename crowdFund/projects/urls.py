from . import views
from django.urls import path

urlpatterns = [
    path('/add', views.addProject, name='addProject'),
    path('/education', views.edu_category, name='education'),
    path('/entertainment', views.entertainment_category, name='entertainment'),
    path('/sports', views.sports_category, name='sports'),
    path('/fashon', views.fashon_category, name='fashon'),

]
