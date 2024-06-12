from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import add_courses

# Create your views here.
def index(request):
    Data =add_courses.objects.all()
    return render(request,'index.html',{"Data":Data})

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')



def Manage_Feedback(request):
    return render(request,'Manage_Feedback.html')

def Manage_Enquiry_details(request):
    return render(request,'Manage_Enquiry_details.html')


def add_enquiry(request):
    return render(request,'add_enquiry.html')


def addenquiry(request):

    if request.method == "POST":
        e_name=request.POST["e_name"]
        e_email=request.POST["e_email"]
        e_subject=request.POST["e_subject"]
        e_message=request.POST["e_message"]
        data=add_enquiry(e_name=e_name,e_email=e_email,e_subject=e_subject,e_message=e_message)
        data.save()
        return redirect("/Manage_Courses")
    else:
        
        return redirect("/Manage_Courses")
#course 

def feedback(request):
    return render(request,'feedback.html')

def add_feedback(request):
    return render(request,'add_feedback.html')

def enquiry(request):
    return render(request,'enquiry.html')



#course
def Add_courses(request):
    return render(request,'add_courses.html')

def addCourse(request):
    if request.method == "POST":
        Course_name=request.POST["Course_name"]
        Details= request.POST["Details"]
        Fees=request.POST["Fees"]
        Duration=request.POST["Duration"]
        Image=request.POST["Image"]
        Mode=request.POST["Mode"]
        data=add_courses(Course_name=Course_name,Details=Details,Fees=Fees,Duration=Duration,Image=Image,Mode=Mode)
        data.save()
        
        return redirect("/Manage_Courses")
    else:
        
        return redirect("/Manage_Courses")
#course list
def Manage_Courses(request):
    Data =add_courses.objects.all()
    return render(request,"Manage_Courses.html",{"Data":Data})
    


def Register_page(request):
    return render(request,"Register_page.html")