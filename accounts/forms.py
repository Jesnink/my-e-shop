from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.views.generic.edit import FormView


class CustomUserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
                 'class':'form-control',
                
             }))
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={
                 'class':'form-control',
                
             }))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
                 'class':'form-control',
                 
             }))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={
                 'class':'form-control',
                 
             }))


    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'username':forms.TextInput(
                attrs={'class':'form-control'}
            )
        }

class LoginForm(AuthenticationForm):
    username=UsernameField(label='Username', widget=forms.TextInput(attrs={
                 'class':'form-control',
                 'autofocus':True,
             }))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
                 'class':'form-control',
                 
             }))
            
class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={
                 'class':'form-control',
                 
             }))
    new_password1= forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={
                 'class':'form-control',
                 
             }))
    new_password2= forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={
                 'class':'form-control',
                 
             }))
    
class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
                 'class':'form-control',
                
             }))

class SetPasswordForm(SetPasswordForm):
    new_password1= forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={
                 'class':'form-control',
                 
             }))
    new_password2= forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={
                 'class':'form-control',
                 
             }))
    
