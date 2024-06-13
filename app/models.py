from django.db import models

# OnlineCourses
# add course
class add_courses(models.Model):
    Course_name=models.CharField(max_length=50,unique='true')
    Details=models.CharField(max_length=100)
    Fees=models.IntegerField()
    Duration=models.CharField(max_length=50)
    Image=models.CharField(max_length=50)
    Mode=models.CharField(max_length=10)

 #add enquiry   
class add_enquiry(models.Model):
    e_name=models.CharField(max_length=50)
    e_email=models.CharField(max_length=50)
    e_subject=models.CharField(max_length=100)
    e_message=models.CharField(max_length=50)

#feedback
    Feedback_name=models.CharField(max_length=50,unique='true')
    Email=models.CharField(max_length=100)
    Phone_number=models.IntegerField(10)
    you_satisfied_with_our_services_Yes_No=models.CharField(max_length=50)
    Your_Suggestion=models.CharField(max_length=50)

#add users
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Profession=models.CharField(max_length=100)
    Email=models.CharField(max_length=50)
    Country_code=models.CharField(max_length=100)
    Contact_number=models.CharField(max_length=50)
    Password=models.CharField(max_length=100)
    Confirm_password=models.CharField(max_length=50)

#add payment

#report