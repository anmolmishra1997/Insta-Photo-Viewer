from django import forms
from django.forms import ModelForm
from .models import Insta_User


class Insta_UserForm(ModelForm):

    class Meta:
        model = Insta_User
        fields=['userid','username','full_name','profile_picture','access_token']        
