from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),    
        path('home', views.home, name='home'),    
        path('list_users', views.list_users, name='list_users'),    

    path("",views.registeration,name="regesteration"),
    path('index/<userEmail_id>', views.index, name='index'),
    path("verification",views.verification,name="verification"),
    path("view",views.View,name="view"),
    path("view_project/<userEmail_id>",views.view_project,name="view_project"),
    path("update_user/<userEmail_id>",views.update_user,name="update_user"),




]

