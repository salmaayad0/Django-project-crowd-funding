from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=15)
    confirm_password=models.CharField(max_length=15)
    image=models.ImageField(upload_to="photos/%y/%m/%d", blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^(00201|\+201|01)[0-2,5]{1}[0-9]{8}$', 
                                 message="Phone number must be entered in the format:010|012|015")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.first_name
    

class Login(models.Model):
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=15)
    
    def __str__(self):
        return self.email
    