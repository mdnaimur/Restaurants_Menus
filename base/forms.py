from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Employees


# User Registration  
class EmployeesRegistrationFrom(UserCreationForm):
    class Meta:
        model= User
        fields = ["username", "email", "password1", "password2"]