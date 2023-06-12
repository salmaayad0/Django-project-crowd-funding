from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),
<<<<<<< HEAD
        path('index', views.index, name='index'),

      path("verification",views.verification,name="verification"),

  path("",views.registeration,name="regesteration"),

=======
    path("",views.registeration,name="regesteration"),
    path('index', views.index, name='index'),
    path("verification",views.verification,name="verification"),
>>>>>>> 9bc522e9a3258eb9f6dc9e7a0f8db2b4ded41120

]

