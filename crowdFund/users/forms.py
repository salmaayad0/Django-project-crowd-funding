from django import forms
from .models import Login,Users

class LoginForm(forms.ModelForm):
    password = forms.CharField(
        label='Password', 
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password'}),
    )

    class Meta:
        model = Login
        fields = ['email']

        
class RegForm(forms.ModelForm):
    password = forms.CharField(
        label='Password', 
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password'}),
    )
    
    confirm_password = forms.CharField(
        label='Confirm Password', 
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password'}),
    )
    
    class Meta:
        model=Users
        fields=fields = ['first_name','last_name','email','image', 'phone_number']