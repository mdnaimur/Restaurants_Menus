from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',views.EmployeesRegistrationFromView.as_view(),name='user_registration'),
    path('login/',views.UserLogin,name='login'),
    path('logout/',views.UserLogOut,name='logout'),
]