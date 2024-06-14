"""
URL configuration for OnlineCourses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
     path('', views.index, name='index'),
     path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
     path('Manage_Courses', views.Manage_Courses, name='Manage_Courses'),
     path('Manage_User', views.Manage_User, name='Manage_User'),
     path('add_users', views.add_users, name='add_users'),
     path('Manage_Feedback', views.Manage_Feedback, name='Manage_Feedback'),
     path('Manage_Enquiry_details', views.Manage_Enquiry_details, name='Manage_Enquiry_details'),
     path('add_enquiry', views.add_enquiry, name='add_enquiry'),
     path('enquiry', views.enquiry, name='enquiry'),
     path('addenquiry', views.addenquiry, name='addenquiry'),
     path('feedback', views.feedback, name='feedback'),
     path('add_feedback',views.add_feedback, name='add_feedback'),
     path('Add_courses', views.Add_courses, name='Add_courses'),
     path('addCourse', views.addCourse, name='addCourse'),
     path('Register_page', views.Register_page, name='Register_page'),
     path('Customer_profile', views.Customer_profile, name='Customer_profile'),
     path('Resources', views.Resources, name='Resources'),
     path('Get_Quotes', views.Get_Quotes, name='Get_Quotes'),
     path('Solutions', views.Solutions, name='Solutions'),
     path('It_Topics', views.It_Topics, name='It_Topics'),
     path("logout", views.logout, name='login')
     


]
