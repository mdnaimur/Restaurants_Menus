from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import EmployeesRegistrationFrom


# Create your views here.
def index(request):
    return render(request,'index.html')


# User Registraion
class EmployeesRegistrationFromView(View):

    def get(self,request):
        form = EmployeesRegistrationFrom
        return render(request,'user_auth/registration.html',locals())
    
    def post(self,request):
        form = EmployeesRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations! User Register Successfully')
            return render(request,'index.html',locals())
        else:
            messages.warning(request,'Invalid Input Data or Empty!!')
            return render(request,'user_auth/registration.html',locals())
        
    
# User Login
        
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exits.')
        user = authenticate(request,username=username,password=password)
        
        #user match nor not
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome!! you have successefully Logged In")
            return redirect('index')
        else:
            messages.error(request,'User or password does not exits')
    return render(request,'user_auth/login.html',locals())

#user logout
def UserLogOut(request):
    logout(request)
    messages.warning(request,"Logged Out !!!\n Login again")
    return redirect('login')