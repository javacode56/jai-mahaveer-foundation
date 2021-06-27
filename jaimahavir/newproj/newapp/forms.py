from django import forms
from django.contrib.auth.models import User
from newapp.models import UserProfileInfo,DonorProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('address','profile_pic','amount')



class DonorProfileInfoForm(forms.ModelForm):
    

    class Meta():
        model=DonorProfileInfo
        fields=('username','email','address','mobile','amount')
