from django.contrib.auth.models import User
from django.db import models

# Create your models here.
##create user model parameter

USER_ROLE = (('Owner','Owner'),('Employee','Employee'))

class Employees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)
    user_role = models.CharField(choices=USER_ROLE,max_length=12,default=None)
    image = models.ImageField(null=True,default="avatar.svg",upload_to='emp_pic')
    def __str__(self):
        return self.name
    