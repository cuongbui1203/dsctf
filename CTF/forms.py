from  django.contrib.auth import *
from django import forms
from CTF.models import *

# creating a form
class NewUserForm(forms.Form):
    email = forms.CharField(max_length=200,required=True)
    username = forms.CharField(max_length=200)
    firstName = forms.CharField(max_length=200)
    lastName = forms.CharField(max_length=200)
    # roll_number = forms.IntegerField(
    #     help_text="Enter 6 digit roll number"
    # )
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User