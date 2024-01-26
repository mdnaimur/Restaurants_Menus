from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Employees


# User Registration  
class EmployeesRegistrationFrom(UserCreationForm):
    class Meta:
        model= User
        fields = ["username", "email", "password1", "password2"]


class EmployeesProfile(ModelForm):
    class Meta:
        model = Employees
        fields =  '__all__'
        exclude = ['user','email']