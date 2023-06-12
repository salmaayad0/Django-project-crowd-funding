from . import views
from django.urls import path

urlpatterns = [
    path('',views.registeration,name ="regesteration"),
    path('login', views.login, name ='login'),
    path('index', views.index, name ='index'),
    path('verification',views.verification,name ="verification"),
    path('profile/<email>',views.userProfile,name ="profile")
]

