from django import forms
from .models import *
from django.contrib.auth.models import User



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['Name','Locality','City','ZipCode','State']
        widgets={
            'Name':forms.TextInput(attrs={
            'class':'form-control'
                
            }),
            'Locality':forms.TextInput(attrs={
            'class':'form-control'
                
            }),
            'City':forms.TextInput(attrs={
            'class':'form-control'
                
            }),
            'ZipCode':forms.NumberInput (attrs={
                'class':'form-control'
                
            }),
            'State':forms.Select(attrs={
            'class':'form-control'
                
            })
        }
