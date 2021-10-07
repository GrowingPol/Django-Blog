from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #Can put a 'required' property, but default is true

    class Meta: #Nested space for configurations
        model = User #model to be used
        fields =['username','email','password1','password2'] #fields to show in our form

class UserUpdateform(forms.ModelForm):
    email = forms.EmailField()  # Can put a 'required' property, but default is true

    class Meta:  # Nested space for configurations
        model = User  # model to be used
        fields = ['username', 'email',]  # fields to show in our form

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['image']