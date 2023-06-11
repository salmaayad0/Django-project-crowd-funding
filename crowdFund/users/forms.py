from django import forms
from .models import Login,Users

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = "__all__"


        
class RegForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'