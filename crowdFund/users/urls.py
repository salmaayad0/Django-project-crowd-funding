from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),    
    path('home/<userEmail_id>', views.home, name='home'),    
    path('list_users', views.list_users, name='list_users'),    
    path("",views.registeration,name="regesteration"),
    path("verification",views.verification,name="verification"),
    path("view",views.View,name="view"),
    path("view_project/<userEmail_id>",views.view_project,name="view_project"),
    path("update_user/<userEmail_id>",views.update_user,name="update_user"),
    path("delete_user/<userEmail_id>",views.delete_user,name="delete_user"),   
    path('profile/<userEmail_id>',views.userProfile,name ="profile"),
    path('addproject', views.addproject, name='addProject')

]

