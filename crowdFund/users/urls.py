from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),
        path('index', views.index, name='index'),

      path("verification",views.verification,name="verification"),

  path("",views.registeration,name="regesteration"),

    path("",views.registeration,name="regesteration"),
    path('index', views.index, name='index'),
    path("verification",views.verification,name="verification"),
    path("view",views.View,name="view"),


]

