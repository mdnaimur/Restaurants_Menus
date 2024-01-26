from django.urls import path

from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('employees/',views.getAllEmployee),
    path('employee/<str:pk>/',views.getEmployee)
]