from django.db import models
from datetime import date
import datetime
from django.db import models
from users.models import Users

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    details = models.TextField(max_length=200)
    category = models.CharField(max_length=50,null=True, blank=True, 
                                choices=[('education','education'),
                                         ('entertainment','entertainment'), 
                                         ('sports','sports'), 
                                         ('fashon','fashon')
                                         ])
    mutliImage = models.ImageField(upload_to="photo/%y/%m/%d", blank=True)
    totalTarget = models.DecimalField(max_digits=6, decimal_places=0)
    tag = models.CharField(max_length=50,null=True, blank=True, 
                                choices=[('education','education'),
                                         ('entertainment','entertainment'), 
                                         ('sports','sports'), 
                                         ('fashon','fashon')
                                         ])
    startDate = models.DateField(default=datetime.date.today)
    # userEmail = models.ForeignKey(Users, on_delete= models.CASCADE)
    email=models.EmailField()
    
