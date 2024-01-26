from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',views.EmployeesRegistrationFromView.as_view(),name='user_registration'),
    path('login/',views.UserLogin,name='login'),
    path('logout/',views.UserLogOut,name='logout'),
    #profile path
    path('profile/',views.EmployeeProfileView.as_view(),name='profile'),
    path('viewprofile/',views.ProfileView.as_view(),name='viewprofile'),
    path('viewprofile/',views.ProfileView.as_view(),name='viewprofile'),
    path('profile_edit/<int:pk>',views.profileEdit,name='editprofile'),
    path('profile_delete/<int:id>',views.profileDelete,name='deleteprofile'),
]

#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
