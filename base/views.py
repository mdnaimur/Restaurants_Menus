from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import EmployeesProfile
from .forms import EmployeesRegistrationFrom
from .models import Employees


# Create your views here.
def index(request):

    try:
        if request.user.is_authenticated:
           employees = Employees.objects.get(user=request.user)
    except:
         messages.error(request,'User not Exist. Please communicate admin!!.')

       # messages.warning(request,'User not Exist. Please communicate admin!!')
    return render(request,'index.html',locals())


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

# Employee Profile View 
class EmployeeProfileView(View):
    
    def get(self,request):
        form = EmployeesProfile()
        return render(request,'EmployeeProfile/profile.html',locals())
    
    def post(self,request):
        form = EmployeesProfile(request.POST,request.FILES)
        #name = form.cleaned_data['name']
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            messages.success(request,'Profile Update Successefully')
            return redirect('index')
        else:
            messages.warning(request,'Invalid Input Date')
        return render(request,'EmployeeProfile/profile.html',locals())  
    

# Employee view list 
class ProfileView(View):
    def get(self,request):
        employees = Employees.objects.get(user=request.user)
        return render(request,'EmployeeProfile/profile_view.html',locals())

# Employee edit 
def profileEdit(request,pk):
    employees = Employees.objects.get(pk=pk)
    form = EmployeesProfile(instance=employees)
    if request.method == 'POST':
        form = EmployeesProfile(request.POST,request.FILES,instance=employees)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated!!')
        return redirect('viewprofile')
    return render(request,'EmployeeProfile/profile.html',locals())

# Employee Delete
def profileDelete(request,id):
    employees = Employees.objects.get(pk=id)
    if request.method == 'POST':
       employees.delete()
       messages.error(request,'Profile Deleted!!')
       return redirect('index')
    return render(request,'EmployeeProfile/profile.html',locals())
# Member add

#Member Edit
#Member Delete
    
#Menu Add

#Item add edit delete

#Order List
    
# Payment List